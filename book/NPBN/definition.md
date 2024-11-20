
# Non-parametric Bayesian Networks

Non-parametric Bayesian Networks (NPBN), also called copula-based Bayesian Networks or Gaussian copula-based Bayesian Networks, are high-dimensional probability distributions composed of a Directed Acyclic Graph (DAG) with nodes and arcs. Nodes represent random variables while arcs represent the direct qualitative dependence between the linked variables. Panel (a) of the Figure below shows an example of a DAG. Panels (b) and (c) show examples of graphs that do NOT meet the conditions to be a DAG.

```{figure} ../figures/example_BN.png

---

---
Examples of graphs: (a) Directed Acyclic Graph, (b) non-Directed Acyclic Graph, and (c) Directed Graph with cycles.
```

Two nodes linked by an arc are called parent and child, being the parent node the predecessor of the child node. For instance, in panel (a) of the Figure above, $X_5$ is the parent of $X_6$ and the child of $X_4$. Also, nodes preceding the parent nodes are called ancestors. This is, $X_3$ is the ancestor of $X_5$ and $X_6$.

The nodes in the DAG are quantified using univariate distribution, which can be either empirical or parametric of any family, as long as it is invertible. The arcs in the DAG are quantified using bivariate Gaussian copulas with conditional or unconditional rank correlations. Thus, **the joint distribution is built in bivariate pieces of dependence**.

Note that since the dependence between each bivariate pair is modelled using a bivariate Gaussian copula, NPBN have the intrinsic limitations of this copula family. Gaussian copulas are symmetric models which cannot model tail dependence. Therefore, **NPBN do not account for tail dependence too.