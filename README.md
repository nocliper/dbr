# Measuring and modelling DBR grown via MOCVD 

 ## Distributed Bragg Reflector (DBR)

 A **Distributed Bragg Reflector (DBR)** is a structure formed from multiple layers of alternating materials with varying refractive index. Each layer boundary causes a partial reflection of an optical wave. For waves whose vacuum wavelength is close to four times the optical thickness of the layers <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\lambda_b" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\lambda_b" title="\lambda_b" /></a>, the many reflections combine with constructive interference, and the layers act as a high-quality reflector. The range of wavelengths that are reflected is called the photonic stop-band. Within this range of wavelengths, light is "forbidden" to propagate in the structure.

 ![Reflection of light in a DBR](img/dbr.png)

 The same principle is used to create multilayer antireflection coatings that are used, including for solar cells. In such coatings, the layer thicknesses are chosen so as to minimise the reflection of <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{R}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{R}" title="\text{R}" /></a> and, accordingly, to maximise the transmission of <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{T}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{T}" title="\text{T}" /></a> (it should be noted that the law <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{T}&space;=&space;1&space;-&space;\text{R}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{T}&space;=&space;1&space;-&space;\text{R}" title="\text{T} = 1 - \text{R}" /></a> holds for dielectric structures)

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=d_1\cdot&space;n_1&space;=&space;d_1\cdot&space;n_1&space;=&space;\frac{\lambda_b}{4}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?d_1\cdot&space;n_1&space;=&space;d_1\cdot&space;n_1&space;=&space;\frac{\lambda_b}{4}" title="d_1\cdot n_1 = d_1\cdot n_1 = \frac{\lambda_b}{4}" /></a>
</p>

 Assuming that a plane light wave is incident strictly perpendicular to the surface of the DBR, the layers are homogeneous and isotropic, the faces of the layers are strictly parallel, then for such a model structure of the DBR we can write the reflection coefficient <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{R}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{R}" title="\text{R}" /></a> in the following rather simple form: - for structures where the refractive indices form the sequence <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;n_0|n_1|n_2|n_1|n_2|...|n_2|n_s" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;n_0|n_1|n_2|n_1|n_2|...|n_2|n_s" title="n_0|n_1|n_2|n_1|n_2|...|n_2|n_s" /></a>

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{R}&space;=&space;\left(\frac{1-\frac{n_s}{n_0}\left(\frac{n_1}{n_2}\right)^{2N}}{1&plus;\frac{n_s}{n_0}\left(\frac{n_1}{n_2}\right)^{2N}}\right)^2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{R}&space;=&space;\left(\frac{1-\frac{n_s}{n_0}\left(\frac{n_1}{n_2}\right)^{2N}}{1&plus;\frac{n_s}{n_0}\left(\frac{n_1}{n_2}\right)^{2N}}\right)^2" title="\text{R} = \left(\frac{1-\frac{n_s}{n_0}\left(\frac{n_1}{n_2}\right)^{2N}}{1+\frac{n_s}{n_0}\left(\frac{n_1}{n_2}\right)^{2N}}\right)^2" /></a>
 </p>

 where <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;N" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;N" title="N" /></a> - is number of <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;n_1&plus;n_2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;n_1&plus;n_2" title="n_1+n_2" /></a> layers

Thus, the larger the ratio of refractive indices <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;n_1/n_2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;n_1/n_2" title="n_1/n_2" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;N" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;N" title="N" /></a>, the higher the reflection coefficient of the DBR. With an increase in the number of layers, the region of high reflection narrows, the peak <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{R}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{R}" title="\text{R}" /></a> becomes flatter and acquires the form of a plateau, and the magnitude of reflection increases. Plateau width <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\Delta\lambda" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\Delta\lambda" title="\Delta\lambda" /></a> i.e. stop-band depends on the difference in the refractive indices of the layers in accordance with the expression:

<p align="center">
 <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\Delta\lambda&space;=&space;\frac{2\lambda_b\cdot\Delta&space;n}{\pi\cdot&space;n_{eff}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\Delta\lambda&space;=&space;\frac{2\lambda_b\cdot\Delta&space;n}{\pi\cdot&space;n_{eff}}" title="\Delta\lambda = \frac{2\lambda_b\cdot\Delta n}{\pi\cdot n_{eff}}" /></a>
 </p>

 where <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\Delta&space;n&space;=&space;n_1&space;-&space;n_2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\Delta&space;n&space;=&space;n_1&space;-&space;n_2" title="\Delta n = n_1 - n_2" /></a>; <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;n_{eff}&space;=&space;2\left(\frac{1}{n_1}&plus;\frac{1}{n_2}\right)^{-1}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;n_{eff}&space;=&space;2\left(\frac{1}{n_1}&plus;\frac{1}{n_2}\right)^{-1}" title="n_{eff} = 2\left(\frac{1}{n_1}+\frac{1}{n_2}\right)^{-1}" /></a>

 ## Epitaxial layers thickness calculation

Due to the centrally symmetric design of the reactor growth chamber, it is possible to build a profile along the radius of the chamber on which two plates lie. Thus, using the experimental data for two samples, it is possible to judge the uniformity of the growth process.

![](img/epitaxy_chamber.png)

Method based on mapping whole substrate. A reflectivity spectrum is taken at each point on substrate surface. Data obtained on line between <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;{300}^\circ" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;{300}^\circ" title="{300}^\circ" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;{120}^\circ" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;{120}^\circ" title="{120}^\circ" /></a> of <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Al}_{0.6}\text{Ga}_{0.4}\text{As}\text{&space;/&space;}&space;\text{AlAs}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Al}_{0.6}\text{Ga}_{0.4}\text{As}\text{&space;/&space;}&space;\text{AlAs}" title="\text{Al}_{0.6}\text{Ga}_{0.4}\text{As}\text{ / } \text{AlAs}" /></a> layers on two <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\text{Ge}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\text{Ge}" title="\text{Ge}" /></a> substrates:

![](M1/M1_1.bmp)

## Transfer-matrix method

There are two waves at each point: one propagates to the right <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;E^R" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;E^R" title="E^R" /></a>, the second to the left <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;E^L" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;E^L" title="E^L" /></a>. Then the vector has two elements:

![](img/layers.png)

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;E&space;=&space;\begin{pmatrix}&space;E^R&space;\\&space;E^L\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;E&space;=&space;\begin{pmatrix}&space;E^R&space;\\&space;E^L\end{pmatrix}" title="E = \begin{pmatrix} E^R \\ E^L\end{pmatrix}" /></a>
</p>

For any two points, the vectors will be connected by a certain linear expression that takes into account the propagation of light through the medium and through the boundaries of two media. This expression can be written using matrices. Basically, we need two matrices. The first <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\textbf{M}_1" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\textbf{M}_1" title="\textbf{M}_1" /></a> connects the vectors to the left and to the right of the interface. The second <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\textbf{M}_2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\textbf{M}_2" title="\textbf{M}_2" /></a> describes the propagation of a wave in a homogenous medium (between interfaces).

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\begin{pmatrix}&space;E^R_2&space;\\&space;E^L_2\end{pmatrix}&space;=&space;\textbf{M}_1\cdot&space;\begin{pmatrix}&space;E^R_1&space;\\&space;E^L_1\end{pmatrix},&space;\,\,\,&space;\begin{pmatrix}&space;E^R_3&space;\\&space;E^L_3\end{pmatrix}&space;=&space;\textbf{M}_2\cdot&space;\begin{pmatrix}&space;E^R_3&space;\\&space;E^L_3\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\begin{pmatrix}&space;E^R_2&space;\\&space;E^L_2\end{pmatrix}&space;=&space;\textbf{M}_1\cdot&space;\begin{pmatrix}&space;E^R_1&space;\\&space;E^L_1\end{pmatrix},&space;\,\,\,&space;\begin{pmatrix}&space;E^R_3&space;\\&space;E^L_3\end{pmatrix}&space;=&space;\textbf{M}_2\cdot&space;\begin{pmatrix}&space;E^R_3&space;\\&space;E^L_3\end{pmatrix}" title="\begin{pmatrix} E^R_2 \\ E^L_2\end{pmatrix} = \textbf{M}_1\cdot \begin{pmatrix} E^R_1 \\ E^L_1\end{pmatrix}, \,\,\, \begin{pmatrix} E^R_3 \\ E^L_3\end{pmatrix} = \textbf{M}_2\cdot \begin{pmatrix} E^R_2 \\ E^L_2\end{pmatrix}" /></a>
</p>

вывод
<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=E^L_1&space;=&space;\frac{n_1-n_2}{n_1&plus;n_2},\,\,\,E^R_2&space;=&space;\frac{2&space;n_1}{n_1&plus;n_2}," target="_blank"><img src="https://latex.codecogs.com/svg.latex?E^L_1&space;=&space;\frac{n_1-n_2}{n_1&plus;n_2},\,\,\,E^R_2&space;=&space;\frac{2&space;n_1}{n_1&plus;n_2}," title="E^L_1 = \frac{n_1-n_2}{n_1+n_2},\,\,\,E^R_2 = \frac{2 n_1}{n_1+n_2}," /></a>
</p>

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=E^R_2&space;=&space;\frac{n_2-n_1}{n_2&plus;n_1},\,\,\,E^L_1&space;=&space;\frac{2&space;n_2}{n_2&plus;n_1}." target="_blank"><img src="https://latex.codecogs.com/svg.latex?E^R_2&space;=&space;\frac{n_2-n_1}{n_2&plus;n_1},\,\,\,E^L_1&space;=&space;\frac{2&space;n_2}{n_2&plus;n_1}." title="E^R_2 = \frac{n_2-n_1}{n_2+n_1},\,\,\,E^L_1 = \frac{2 n_2}{n_2+n_1}." /></a>
</p>

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{pmatrix}&space;E^R_2&space;\\&space;E^L_2\end{pmatrix}&space;=\frac{1}{2&space;n_2}&space;\begin{pmatrix}&space;n_2&space;&plus;n_1&space;&&space;n_2-n_1\\&space;n_2-n_1&space;&&space;n_2&space;&plus;n_1\end{pmatrix}\cdot\begin{pmatrix}&space;E^R_1&space;\\&space;E^L_1\end{pmatrix}&space;=\textbf{M}_1\cdot&space;\begin{pmatrix}&space;E^R_1&space;\\&space;E^L_1\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{pmatrix}&space;E^R_2&space;\\&space;E^L_2\end{pmatrix}&space;=\frac{1}{2&space;n_2}&space;\begin{pmatrix}&space;n_2&space;&plus;n_1&space;&&space;n_2-n_1\\&space;n_2-n_1&space;&&space;n_2&space;&plus;n_1\end{pmatrix}\cdot\begin{pmatrix}&space;E^R_1&space;\\&space;E^L_1\end{pmatrix}&space;=\textbf{M}_1\cdot&space;\begin{pmatrix}&space;E^R_1&space;\\&space;E^L_1\end{pmatrix}" title="\begin{pmatrix} E^R_2 \\ E^L_2\end{pmatrix} =\frac{1}{2 n_2} \begin{pmatrix} n_2 +n_1 & n_2-n_1\\ n_2-n_1 & n_2 +n_1\end{pmatrix}\cdot\begin{pmatrix} E^R_1 \\ E^L_1\end{pmatrix} =\textbf{M}_1\cdot \begin{pmatrix} E^R_1 \\ E^L_1\end{pmatrix}" /></a>
</p>

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{pmatrix}&space;E^R_4&space;\\&space;E^L_4\end{pmatrix}&space;=\frac{1}{2&space;n_2}&space;\begin{pmatrix}&space;e^{i&space;k&space;L}&space;&0\\&space;0&space;&&space;e^{-i&space;k&space;L}\end{pmatrix}\cdot\begin{pmatrix}&space;E^R_1&space;\\&space;E^L_1\end{pmatrix}&space;=\textbf{M}_2\cdot&space;\begin{pmatrix}&space;E^R_3&space;\\&space;E^L_3\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{pmatrix}&space;E^R_4&space;\\&space;E^L_4\end{pmatrix}&space;=\frac{1}{2&space;n_2}&space;\begin{pmatrix}&space;e^{i&space;k&space;L}&space;&0\\&space;0&space;&&space;e^{-i&space;k&space;L}\end{pmatrix}\cdot\begin{pmatrix}&space;E^R_1&space;\\&space;E^L_1\end{pmatrix}&space;=\textbf{M}_2\cdot&space;\begin{pmatrix}&space;E^R_3&space;\\&space;E^L_3\end{pmatrix}" title="\begin{pmatrix} E^R_4 \\ E^L_4\end{pmatrix} =\frac{1}{2 n_2} \begin{pmatrix} e^{i k L} &0\\ 0 & e^{-i k L}\end{pmatrix}\cdot\begin{pmatrix} E^R_1 \\ E^L_1\end{pmatrix} =\textbf{M}_2\cdot \begin{pmatrix} E^R_3 \\ E^L_3\end{pmatrix}" /></a>
</p>
where <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;k&space;=&space;\frac{2\pi&space;n}{\lambda}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;k&space;=&space;\frac{2\pi&space;n}{\lambda}" title="k = \frac{2\pi n}{\lambda}" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;n" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;n" title="n" /></a> – refrective index, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\lambda" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\lambda" title="\lambda" /></a> – wavelenght, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;L" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;L" title="L" /></a> – layer thickness.

![](img/layers2.png)

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{pmatrix}&space;E^R_B&space;\\&space;E^L_B\end{pmatrix}&space;=&space;\textbf{M}_1^{(1)}\textbf{M}_2^{(1)}&space;\textbf{M}_1^{(2)}\textbf{M}_2^{(2)}&space;\textbf{M}_1^{(3)}\textbf{M}_2^{(3)}&space;\textbf{M}_1^{(4)}\textbf{M}_2^{(4)}&space;\cdot&space;\begin{pmatrix}&space;E^R_A&space;\\&space;E^L_A\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{pmatrix}&space;E^R_B&space;\\&space;E^L_B\end{pmatrix}&space;=&space;\textbf{M}_1^{(1)}\textbf{M}_2^{(1)}&space;\textbf{M}_1^{(2)}\textbf{M}_2^{(2)}&space;\textbf{M}_1^{(3)}\textbf{M}_2^{(3)}&space;\textbf{M}_1^{(4)}\textbf{M}_2^{(4)}&space;\cdot&space;\begin{pmatrix}&space;E^R_A&space;\\&space;E^L_A\end{pmatrix}" title="\begin{pmatrix} E^R_B \\ E^L_B\end{pmatrix} = \textbf{M}_1^{(1)}\textbf{M}_2^{(1)} \textbf{M}_1^{(2)}\textbf{M}_2^{(2)} \textbf{M}_1^{(3)}\textbf{M}_2^{(3)} \textbf{M}_1^{(4)}\textbf{M}_2^{(4)} \cdot \begin{pmatrix} E^R_A \\ E^L_A\end{pmatrix}" /></a>
</p>

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{pmatrix}&space;t\\&space;0\end{pmatrix}&space;=&space;M&space;\begin{pmatrix}&space;1&space;\\&space;r\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{pmatrix}&space;t\\&space;0\end{pmatrix}&space;=&space;M&space;\begin{pmatrix}&space;1&space;\\&space;r\end{pmatrix}" title="\begin{pmatrix} t\\ 0\end{pmatrix} = M \begin{pmatrix} 1 \\ r\end{pmatrix}" /></a>
</p>

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=r&space;=&space;\frac{M_{21}}{M_{11}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?r&space;=&space;\frac{M_{21}}{M_{11}}" title="r = \frac{M_{21}}{M_{11}}" /></a>
</p>

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=R&space;=&space;r^2" target="_blank"><img src="https://latex.codecogs.com/svg.latex?R&space;=&space;r^2" title="R = r^2" /></a>
</p>

## Chebyshev polynomial of second kind

<p align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=\textbf{M}^N&space;=&space;\begin{pmatrix}&space;a&space;&&space;b\\&space;c&&space;d\end{pmatrix}^N=&space;\begin{pmatrix}&space;a\cdot&space;U_{N-1}(p)&space;-&space;U_{N-2}(p)&space;&&space;b\cdot&space;U_{N-1}(p)\\&space;c\cdot&space;U_{N-1}(p)&&space;d\cdot&space;U_{N-1}(p)&space;-&space;U_{N-2}(p)\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\textbf{M}^N&space;=&space;\begin{pmatrix}&space;a&space;&&space;b\\&space;c&&space;d\end{pmatrix}^N=&space;\begin{pmatrix}&space;a\cdot&space;U_{N-1}(p)&space;-&space;U_{N-2}(p)&space;&&space;b\cdot&space;U_{N-1}(p)\\&space;c\cdot&space;U_{N-1}(p)&&space;d\cdot&space;U_{N-1}(p)&space;-&space;U_{N-2}(p)\end{pmatrix}" title="\textbf{M}^N = \begin{pmatrix} a & b\\ c& d\end{pmatrix}^N= \begin{pmatrix} a\cdot U_{N-1}(p) - U_{N-2}(p) & b\cdot U_{N-1}(p)\\ c\cdot U_{N-1}(p)& d\cdot U_{N-1}(p) - U_{N-2}(p)\end{pmatrix}" /></a>
</p>
where <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;p&space;=&space;\frac{a&plus;d}{2}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;p&space;=&space;\frac{a&plus;d}{2}" title="p = \frac{a+d}{2}" /></a>; <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;U_N(x)&space;=&space;\frac{sin\left[(N&plus;1)\right]arccos(x)}{sin\left[arccos(x)\right]}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;U_N(x)&space;=&space;\frac{sin\left[(N&plus;1)\right]arccos(x)}{sin\left[arccos(x)\right]}" title="U_N(x) = \frac{sin\left[(N+1)\right]arccos(x)}{sin\left[arccos(x)\right]}" /></a>
