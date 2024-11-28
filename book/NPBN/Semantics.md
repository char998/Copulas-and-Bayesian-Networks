
# Semantics of NPBNs

In previous section, you have seen how to assign (un)conditional rank correlations to a DAG and the rank correlation matrix as a representation of the NPBN. If you want to read more about NPBN and their semantics, we refer you to Pearl (1988)[^pearl].

In this section, you will see the meaning of the DAG in terms of (un)conditional dependence or independence and how that translates to the rank correlation matrix. To do so, we will analyze the three basic cases of NPBN on 3 nodes shown in the Figure below.

```{figure} ./figures/DAGs.png

---

---
Cases of DAGs on 3 nodes.
```

## Case (a): 1 $\rightarrow$ 2 $\rightarrow$ 3

```{figure} ./figures/case_a.png

---

---

```

In this first case, $X_1$ is the parent of $X_2$ and $X_2$ is the parent of $X_3$. The first thing that we can derive from the DAG is that $X_1 \cancel{\perp} X_2$ and $X_2 \cancel{\perp} X_3$ as there are direct statements of the dependence between the variables. Moreover, due to the direction of the arrows in this case as a sequence, $X_1 \cancel{\perp} X_3$. This is, the dependence between $X_1$ and $X_3$ is inferred through the DAG. However, $X_1$ and $X_3$ become independent once I know the value of $X_2$ (mathematically $X_1 \perp X_3|X_2$). Therefore, the rank correlation matrix that would be derived from this NPBN would be complete as

$$
\begin{pmatrix}
1 \ \ \ r_{12} \ \ \ r_{13}\\
r_{21} \ \ 1 \ \ \ r_{23} \\
r_{31} \ \ r_{32} \ \ \ 1\\
\end{pmatrix}
$$

**Let's see it with examples!**

The first example is with a discrete Bayesian Network (DBN) and, thus, with discrete variables. In the Figure below, you have a DBN with the following nodes: (1) the probability that it snows, (2) the probability that the train is late, and (3) the probability that you, as train used, are late. If it snows, it is much more likely that the train is late due to the metheorological conditions and, thus, that you are also late. Therefore, (1) and (3) are not independent, as we saw before. However, once I know that the train is late, the probability of being late is not affected any more about the fact that it snows or not. This is, (1) and (3) become independent once I know (2), as we saw before

```{figure} ./figures/discrete_case_a.png

---

---

```

Let's make the variables continuous now. In the Figure below, you have a NPBN with the following random variables in the nodes: (1) accumulated milimeters of snow a day, (2) minutes of delay of a train, and (3) minutes of delay to my destination. They are, thus, continuous variables quantified with continuous distribution functions. 

```{figure} ./figures/continuous_case_a.png

---

---

```

If the probability of high values of snow increase for a day, the probabilitiy of a higher delay of the train also increases and, together with it, also the probability of higher delay for me. However, once I know how many minutes the train is late, the amount of snow does not have an influence on my expected delay.