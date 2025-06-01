import jax
import jax.numpy as jnp
from jax import random

import numpy as np

import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS, log_likelihood

# ------------------------------
# ガウス関数 g(τ; μ, σ^2)
# ------------------------------
def gaussian(tau: jnp.ndarray, mu: float, sigma: float) -> jnp.ndarray:
    # return jnp.exp(-0.5 * ((tau - mu) / sigma) ** 2) / (sigma * jnp.sqrt(2 * jnp.pi))
    return jnp.exp( -0.5 * ((tau - mu) / sigma) ** 2.0 )

# ------------------------------
# φ_K(τ_i; θ) の計算
# φ_K(τ_i) = Σ h_k * g(τ_i; μ_k, σ_k^2)
# ------------------------------
def calc_phi_K(tau: jnp.ndarray, h: jnp.ndarray, mu: jnp.ndarray, sigma: jnp.ndarray) -> jnp.ndarray:
    """
    混合ガウスによる φ_K を計算
    tau: 離散化された時定数 (N,)
    h, mu, sigma: 混合成分のパラメータ (K,)
    戻り値: φ_K(tau_i) の値 (N,)
    """
    K = h.shape[0]
    
    # 各ガウス成分の値を (K, N) で計算
    gaussians = jnp.stack([gaussian(tau, mu[k], sigma[k]) for k in range(K)], axis=0)  # (K, N)
    
    # 混合係数で重み付けして合計 → (N,)
    phi = jnp.dot(h, gaussians)  # (N,)
    
    return phi

# ------------------------------
# f_K(t; θ) の計算
# f_K(t) = b + Δ Σ φ_K(τ_i) * exp(-t / τ_i)
# ------------------------------
def calc_f_K(t: jnp.ndarray, tau: jnp.ndarray, b: float, h: jnp.ndarray, mu: jnp.ndarray, sigma: jnp.ndarray) -> jnp.ndarray:
    """
    離散時定数モデルに基づく関数f_Kの評価
    t: 入力時間軸 (M,)
    tau: 離散時定数 (N,)
    params: モデルパラメータ
    戻り値: f_K(t) の値 (M,)
    """
    delta = tau[1] - tau[0]  # τの刻み幅 Δ
    phi = calc_phi_K(tau, h, mu, sigma)  # (N,)
    
    # 各時間tに対して積分近似を計算: f(t) = b + Δ Σ φ_K(τ_i) * exp(-t / τ_i)
    exp_decay = jnp.exp(-jnp.outer(t, 1.0 / tau))  # (M, N)
    weighted_sum = delta * jnp.dot(exp_decay, phi)  # (M,)
    
    return b + weighted_sum  # (M,)

# --- ベイズモデルの定義 ---
def model(t: jnp.ndarray, y_obs: jnp.ndarray, tau: jnp.ndarray, K: int):
    # ハイパーパラメータに基づいて事前分布を設定
    b = numpyro.sample("b", dist.Normal(0.0, 1.0))
    
    h_raw = numpyro.sample("h", dist.Uniform(0, 1.5).expand([K]))
    mu = numpyro.sample("mu", dist.Uniform(tau.min(), tau.max()).expand([K]))
    sigma = numpyro.sample("sigma", dist.LogNormal(-1.0, 1.0).expand([K]))
    
    # モデル予測値
    f = numpyro.deterministic('f', calc_f_K(t, tau, b, h_raw, mu, sigma))
    
    
    # 観測ノイズ付きの尤度
    sigma_y = numpyro.sample("sigma_y", dist.HalfNormal(0.1))
    numpyro.sample("obs", dist.Normal(f, sigma_y), obs=y_obs)
