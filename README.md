## 時定数分布のベイズ推論

時定数が連続分布として含まれる指数減衰モデルは下記のように表現できる：

$$
f(t; \theta) = b + \int{ \phi(\tau; \theta) \exp{ \left( - \frac{t}{\tau}\right) } \mathrm{d} \tau}
$$

上記の式の時定数の空間を離散化し，時定数の連続分布が混合ガウス関数で表現できると仮定すると：

$$
f_K(t; \theta) = b + \Delta \sum_{i=1}^{N}{ \phi_K(\tau_i; \theta) \exp{ \left( - \frac{t}{\tau_i}\right) }  } \\
\text{where } \:\: \phi_{K}(\tau_i; \theta)=\sum_{k=1}^{K}{ h_k g(\tau_i; \mu_k, \sigma^2_k)}
$$

ここで，$`g(\tau_i; \mu_k, \sigma^2_k)`$はガウス関数である．$`\Delta`$は時定数の空間を離散化したときの刻み幅である．求めるパラメータは$`\theta=\{ b, h, \mu, \sigma \}`$である．

