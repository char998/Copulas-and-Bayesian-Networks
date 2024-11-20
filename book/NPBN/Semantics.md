
# Semantics

Each Directed Acyclic Graph (DAG) with conditional or unconditional correlations on the arcs can be represented by a _rank correlation matrix_. In this section, the definition of rank correlation matrix, the semantics of the DAGs and their implication in the representative rank correlation matrix are discussed.  

## Rank correlation matrix

A rank correlation matrix representing a DAG with conditional or unconditional correlations is a $n \times n$ matrix, where $n$ represents the number of nodes in the DAG. Each element is a rank correlation computed between the random variables whose indexes correspond to the indexes of the rows and columns. This is, a rank correlation matrix for a 4-dimensions problem is givne by

$$
\begin{pmatrix}
r_{11} \ r_{12} \ r_{13} \ r_{14} \\
r_{21} \ r_{22} \ r_{23} \ r_{24} \\
r_{31} \ r_{32} \ r_{33} \ r_{34} \\
r_{41} \ r_{42} \ r_{43} \ r_{44} 
\end{pmatrix} = 
\begin{pmatrix}
1 \ r_{12} \ r_{13} \ r_{14} \\
r_{21} \ 1 \ r_{23} \ r_{24} \\
r_{31} \ r_{32} \ 1 \ r_{34} \\
r_{41} \ r_{42} \ r_{43} \ 1
\end{pmatrix}
$$

The rank correlation computed between one random variable and itself is equal to one. Thus, the diagonal of the rank correlation matrix is populated with 1. Also, it should be noted that the rank correlation matrix is symmetric as $r_{12} = r_{21}$.

Note that it is also possible to compute a rank correlation matrix from observations. This is, just calculating the rank correlations between each pair of variables based on the observations and putting it in matricial shape.

```{admonition} "How do I want my rank correlation matrix of the DAG to be?"
:class: tip
When deriving a rank correlation matrix from a DAG that we have defined, we get the rank correlations that we are imposing between the random variables that we are studying. Therefore, we would like that those rank correlations are similar to those that we observed in our dataset. The comparison of the rank correlation matrix that we compute from the observations and that derived from the DAG gives us an idea of how good is our model.

You will see more on this topic in section on assessment and validation.
```

## Assigning correlations to the arcs

Each arc in the DAG is quantified through a conditional or unconditional rank correlation. But how do we assign them?

Consider that each node $i$ represents a variable $X_i$. $Pa(i)={i_1, ..., i_{p(i)}}$ is the set of parent nodes of the node $i$. The rank correlations associated the arcs $i_{p(i)-k} \to i$ are given by

$$
    \begin{cases}
      r_{i,i_{p(i)}} & \text{$k=0$}\\
      r_{i,i_{p(i)-k}|i_{p(i)}-k+1} & \text{$1 \leq k \leq p(i)-1$}\\
    \end{cases}       
$$

This assignment of (conditional) rank correlations for $i=1,...,n$ results in associating a rank correlation to each arc between parent and child. The following theorem from \cite{HANEA2015} shows that these assignments are independent and uniquely determine the joint distribution for a particular choice of copulae.

\

\textbf{Theorem 1.} \cite{HANEA2015} \label{theorem}Given:
\textit{
\begin{enumerate}
    \item a directed acyclic graph with n nodes specifying conditional independence relationships in an BN;
    \item n variables $X_1, ..., X_n$ assigned to the nodes, with invertible distribution functions $F_1, ..., F_n$;
    \item the specification (\ref{eq:correl_theorem}), $i=1,...n$, of (conditional) rank correlations on the arcs of the BN;
    \item any copula realizing all correlations [-1,1];
    \item the (conditional) independent copula realizing all (conditional) independence relationships encoded by the graph of the BN;
\end{enumerate}}

\textit{the joint distribution of the $n$ variables is uniquely determined. This joint distribution satisfies the characteristic factorization (\ref{eq:density_theorem}) and the conditional rank correlations in (\ref{eq:correl_theorem}) are algebraically independent.}

## Semantics of DAGs

Note that since the dependence between each bivariate pair is modelled using a bivariate Gaussian copula, NPBN have the intrinsic limitations of this copula family. Gaussian copulas are symmetric models which cannot model tail dependence. Therefore, **NPBN do not account for tail dependence too.