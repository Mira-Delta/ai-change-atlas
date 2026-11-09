# Pairwise agreement does not determine majority risk

**Record date:** 2 November 2026. **Evidence type:** finite mathematical construction. **Status:** exactly checkable example; not an LLM experiment and not a claim about observed model populations.

Let three binary classifiers have error indicators \(E_1,E_2,E_3\), and let \(K=E_1+E_2+E_3\). In each distribution below, configurations are exchangeable: conditional on K, all configurations with that many errors are equally likely.

| K | Distribution A | Distribution B |
|---:|---:|---:|
| 0 | 0.55 | 0.45 |
| 1 | 0.15 | 0.45 |
| 2 | 0.30 | 0.00 |
| 3 | 0.00 | 0.10 |

For both distributions, \(E[K]=0.75\), so each classifier has error probability \(0.75/3=0.25\). Also \(E[K(K-1)]=0.60\). By exchangeability, each pair has joint error probability \(0.60/(3\cdot2)=0.10\), giving pairwise error correlation

\[
rac{0.10-(0.25)^2}{0.25(1-0.25)}=0.20.
\]

The majority error probability differs: \(P(K\ge2)=0.30\) in A and \(0.10\) in B. Thus the same individual error rate and pairwise correlation can coexist with distinct higher-order joint error patterns and majority risk.

**Implication:** accuracy, agreement, pairwise correlation, or a derived effective-vote count alone cannot determine majority reliability. This example does not establish that any real model group has either distribution, nor does it show collective agency or consciousness.

**Open question:** Which higher-order dependence statistics and interventions best distinguish genuine interaction benefits from shared errors?
