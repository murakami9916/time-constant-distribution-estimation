## 時定数分布のベイズ推論

時定数が連続分布として含まれる指数減衰モデルは下記のように表現できる：

$$
\begin{equation}
  f(t; \theta) = b + \int{ \phi(\tau; \theta) \exp{ \left( - \frac{t}{\tau}\right) } \mathrm{d} \tau}
\end{equation}
$$

上記の式の時定数の空間を離散化し，時定数の連続分布が混合ガウス関数で表現できると仮定すると：

$$
\begin{eqnarray}
  f_K(t; \theta) = b + \Delta \sum_{i=1}^{N}{ \phi_K(\tau_i; \theta) \exp{ \left( - \frac{t}{\tau_i}\right) }  } \\
  \text{where} \ \ \ \phi_{K}(\tau_i; \theta)=\sum_{k=1}^{K}{ h_k g(\tau_i; \mu_k, \sigma^2_k)}
\end{eqnarray}
$$

ここで，$`g(\tau_i; \mu_k, \sigma^2_k)`$はガウス関数である．$`\Delta`$は時定数の空間を離散化したときの刻み幅である．求めるパラメータは$`\theta=\{ b, h, \mu, \sigma \}`$である．

## 実験結果

### 人工データ

![image](https://github.com/user-attachments/assets/a45f0bd6-f04e-48ab-8298-5cc81088c5a0)

### 推定結果

フィッティング結果

![image](https://github.com/user-attachments/assets/67ce93e9-fb0d-43e3-90d6-bfd6695eed64)

負の対数尤度の密度分布

![image](https://github.com/user-attachments/assets/404f2fd1-821e-4647-a089-ae872837fb03)

時定数分布のMAP解

![image](https://github.com/user-attachments/assets/ceadedba-8f1e-41ff-802e-8a06b5b9be0d)

事後分布: $`\mu_1`$ vs $`\mu_2`$

![image](https://github.com/user-attachments/assets/5cb60115-f174-4ff7-b37c-775b7d90c9b3)

事後分布: $`b`$ vs $`\mu_1`$, $`\mu_2`$

![image](https://github.com/user-attachments/assets/2d47d496-45c1-49f2-8091-138115a7c727)

