# Covariance and Correlation

In many engineering and scientific applications there are multiple variables involved in the issues assessed. In structural engineering, when assessing the health of a structure, we have to take into account the loads imposed as well as the decay of the building materials. In climate science, when trying to study the effect of climate change in agricultural production we have to consider the impact of temperature change, soil moisture and precipitation, amongst others, in vegetation. 

These variables of interest are often "tied" to one another. By imposing loads continiously in a bridge, the materials that consist start losing some of their . And as temperature increases, some of the soil moisture evaporates, which might impact precipitation later. How to assess all these complex relations between variables of interest?

### Covariance

Covariance is a measure of how two variables vary together, so it is a measure of their joint probability. High values of covariance generally mean that there is a strong dependance between variables. The formula for the calculation of covariance is:

$$
\text{Cov}(X_1, X_2) = \mathbb{E}[(X_1 - \mu_{X_1})(X_2 - \mu_{X_2})]
$$

If $Cov(X_1,X_2)>0$ it means that high (low) values of $X_1$ occur together with high (low) values of $X_2$, therefore the covariance is defined as *POSITIVE*.

On the other hand, if $Cov(X_1,X_2)<0$ it means that high (low) values of $X_1$ occur together with low (high) values of $X_2$. In this case the covariance is defined as *NEGATIVE*.

Note that:

$$
Cov(X_i,X_i)=\mathbb{E}([X_i-\mathbb{E}(X_i)]^2) =\sigma^2_i
$$

### Correlation

A simple way to assess statistically whether two variables are related is their (linear) correlation, which describes how change in respect to one another. One of the most popular ways to calculate the correlation is the Pearson correlation r:

$$
\rho = \frac{\sum_{i=1}^{n} (X_{1i} - \bar{X_1})(X_{2i} - \bar{X_2})}{\sqrt{\sum_{i=1}^{n} (X_{1i} - \bar{X_1})^2 \sum_{i=1}^{n} (X_{2i} - \bar{X_2})^2}}
$$

Where:
- $X_{1i}$ and  $X_{2i}$ are the individual data points,
- $\bar{X_1}$ and $\bar{X_2}$ are the means of $X_1$ and $X_2$,
- $n$ is the number of data points.

Pearson correlation is also related to covariance as

$$ 
\rho(X_1,X_2)=\frac{Cov(X_1, X_2)}{\sigma_{X_1} \sigma_{X_2}} 
$$ 

In the plot below you can see and try how the values of $X_1$ and $X_2$ vary together given their correlation. 

<iframe src="../_static/elements/element_correlation.html" width="600" height="400" frameborder="0"></iframe>