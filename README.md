## 時定数分布のベイズ推論

時定数が連続分布として含まれる指数減衰モデルは下記のように表現できる：

$$
\begin{equation}
  f(t; \theta) = b + \int{ \phi(\tau; \theta) \exp{ \left( - \frac{t}{\tau}\right) } \mathrm{d} \tau}
\end{equation}
$$

上記の式の時定数の空間を離散化し，時定数の連続分布が混合ガウス関数で表現できると仮定すると：

$$
\begin{align}
  f_K(t; \theta) = b + \Delta \sum_{i=1}^{N}{ \phi_K(\tau_i; \theta) \exp{ \left( - \frac{t}{\tau_i}\right) }  } \\
  \text{where} \ \ \ \phi_{K}(\tau_i; \theta)=\sum_{k=1}^{K}{ h_k g(\tau_i; \mu_k, \sigma^2_k)}
\end{align}
$$

ここで，$`g(\tau_i; \mu_k, \sigma^2_k)`$はガウス関数である．$`\Delta`$は時定数の空間を離散化したときの刻み幅である．求めるパラメータは$`\theta=\{ b, h, \mu, \sigma \}`$である．

## 実験結果

### 人工データ

![image](https://github.com/user-attachments/assets/a45f0bd6-f04e-48ab-8298-5cc81088c5a0)

### 推定結果

フィッティング結果

![image](https://github.com/user-attachments/assets/67ce93e9-fb0d-43e3-90d6-bfd6695eed64)

負の対数尤度の密度分布

![image](https://github.com/user-attachments/assets/58c8b141-87b8-45b9-bab8-53414f5e38d1)

時定数分布のMAP解

![image](https://github.com/user-attachments/assets/d529fd2f-06b1-4503-9e06-9aca5baba5d8)

事後分布: $`\mu_1`$ vs $`\mu_2`$

![image](https://github.com/user-attachments/assets/04444ced-7aac-4abd-913b-41cb81869828)

事後分布: $`b`$ vs $`\mu_1`$, $`\mu_2`$

![image](https://github.com/user-attachments/assets/ee01de03-d304-4710-9d3a-4e41007d8786)


