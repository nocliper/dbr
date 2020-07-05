# dbr
 Analisys of epitaxial Al(x)Ga(1-x)As

 ## Distributed Bragg Reflector (DBR)

 A **Distributed Bragg Reflector (DBR)** is a structure formed from multiple layers of alternating materials with varying refractive index. Each layer boundary causes a partial reflection of an optical wave. For waves whose vacuum wavelength is close to four times the optical thickness of the layers $\lambda_b$, the many reflections combine with constructive interference, and the layers act as a high-quality reflector. The range of wavelengths that are reflected is called the photonic stop-band. Within this range of wavelengths, light is "forbidden" to propagate in the structure.

 ![Reflection of light in a DBR](img/dbr.png)

 The same principle is used to create multilayer antireflection coatings that are used, including for solar cells. In such coatings, the layer thicknesses are chosen so as to minimise the reflection of $\text{R}$ and, accordingly, to maximise the transmission of $\text{T}$ (it should be noted that the law $\text{T} = 1 - \text{R}$ holds for dielectric structures)

 $$d_1\cdot n_1 = d_1\cdot n_1 = \frac{\lambda_b}{4}$$

 Assuming that a plane light wave is incident strictly perpendicular to the surface of the DBR, the layers are homogeneous and isotropic, the faces of the layers are strictly parallel, then for such a model structure of the DBR we can write the reflection coefficient $R$ in the following rather simple form: - for structures where the refractive indices form the sequence $n_0|n_1|n_2|n_1|n_2|...|n_2|n_s$

 $$\text{R} = \left(\frac{1-\frac{n_s}{n_0}\left(\frac{n_1}{n_2}\right)^{2N}}{1+\frac{n_s}{n_0}\left(\frac{n_1}{n_2}\right)^{2N}}\right)^2$$

 where $N$ - is number of $n_1+n_2$ layers

 Thus, the larger the ratio of refractive indices $n_1/n_2$ and $N$, the higher the reflection coefficient of the DBR. With an increase in the number of layers, the region of high reflection narrows, the peak $R$ becomes flatter and acquires the form of a plateau, and the magnitude of reflection increases. Plateau width $\Delta\lambda$ i.e. stop-band depends on the difference in the refractive indices of the layers in accordance with the expression:

 $$\Delta\lambda = \frac{2\lambda_b\cdot\Delta n}{\pi\cdot n_{eff}}$$

 where $\Delta n = n_1 - n_2$; $n_{eff} = 2\left(\frac{1}{n_1}+\frac{1}{n_2}\right)^{-1}$

 ## Epitaxial layers thickness calculation

Due to the centrally symmetric design of the reactor growth chamber, it is possible to build a profile along the radius of the chamber on which two plates lie. Thus, using the experimental data for two samples, it is possible to judge the uniformity of the growth process.

![](img/epitaxy_chamber.png)

Method based on mapping whole substrate. A reflectivity spectrum is taken at each point on substrate surface. Data obtained on line between ${300}^\circ$ and ${120}^\circ$ of $\text{Al}_{0.6}\text{Ga}_{0.4}\text{As}\text{ / } \text{AlAs}$ layers on two $\text{Ge}$ substrates:

![](M1/M1_1.bmp)

## Transfer-matrix method

There are two waves at each point: one propagates to the right $E^R$, the second to the left $E^L$. Then the vector has two elements:

![](img/layers.png)

$$E = \begin{pmatrix} E^R \\ E^L\end{pmatrix}$$

For any two points, the vectors will be connected by a certain linear expression that takes into account the propagation of light through the medium and through the boundaries of two media. This expression can be written using matrices. Basically, we need two matrices. The first $\textbf{M}_1$ connects the vectors to the left and to the right of the interface. The second $\textbf{M}_2$ describes the propagation of a wave in a homogeneous medium (between interfaces).

$$\begin{pmatrix} E^R_2 \\ E^L_2\end{pmatrix} = \textbf{M}_1\cdot \begin{pmatrix} E^R_1 \\ E^L_1\end{pmatrix}, \,\,\, \begin{pmatrix} E^R_3 \\ E^L_3\end{pmatrix} = \textbf{M}_2\cdot \begin{pmatrix} E^R_3 \\ E^L_3\end{pmatrix}$$

вывод

$$E^L_1 = \frac{n_1-n_2}{n_1+n_2},\,\,\,E^R_2 = \frac{2 n_1}{n_1+n_2},$$

$$E^R_2 = \frac{n_2-n_1}{n_2+n_1},\,\,\,E^L_1 = \frac{2 n_2}{n_2+n_1}.$$

$$\begin{pmatrix} E^R_2 \\ E^L_2\end{pmatrix}
=\frac{1}{2 n_2} \begin{pmatrix} n_2 +n_1 & n_2-n_1\\ n_2-n_1 & n_2 +n_1\end{pmatrix}\cdot\begin{pmatrix} E^R_1 \\ E^L_1\end{pmatrix}
=\textbf{M}_1\cdot \begin{pmatrix} E^R_1 \\ E^L_1\end{pmatrix}$$

$$\begin{pmatrix} E^R_4 \\ E^L_4\end{pmatrix}
=\frac{1}{2 n_2} \begin{pmatrix} e^{i k L} &0\\ 0 & e^{-i k L}\end{pmatrix}\cdot\begin{pmatrix} E^R_1 \\ E^L_1\end{pmatrix}
=\textbf{M}_2\cdot \begin{pmatrix} E^R_3 \\ E^L_3\end{pmatrix}$$
where $k = \frac{2\pi n}{\lambda}$, $n$ – refrective index, $\lambda$ – wavelenght, $L$ – layer thickness.

![](img/layers2.png)

$$\begin{pmatrix} E^R_B \\ E^L_B\end{pmatrix}
= \textbf{M}_1^{(1)}\textbf{M}_2^{(1)} \textbf{M}_1^{(2)}\textbf{M}_2^{(2)}
\textbf{M}_1^{(3)}\textbf{M}_2^{(3)}
\textbf{M}_1^{(4)}\textbf{M}_2^{(4)}
\cdot \begin{pmatrix} E^R_A \\ E^L_A\end{pmatrix}$$

$$\begin{pmatrix} t\\ 0\end{pmatrix}  = M \begin{pmatrix} 1 \\ r\end{pmatrix} $$

$$r = \frac{M_{21}}{M_{11}}$$

$$R = r^2$$

## Chebyshev polynomial of second kind

$$\textbf{M}^N = \begin{pmatrix} a & b\\ c& d\end{pmatrix}^N= \begin{pmatrix} a\cdot U_{N-1}(p) - U_{N-2}(p) & b\cdot U_{N-1}(p)\\ c\cdot U_{N-1}(p)& d\cdot U_{N-1}(p) - U_{N-2}(p)\end{pmatrix}$$
where $p = \frac{a+d}{2}$; $U_N(x) = \frac{sin\left[(N+1)\right]arccos(x)}{sin\left[arccos(x)\right]}$
