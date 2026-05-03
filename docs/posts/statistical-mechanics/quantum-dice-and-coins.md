# Quantum Dice and Coins: A Gentle Introduction to Bose-Einstein and Fermi-Dirac Statistics

**Reference:** James P. Sethna, *Statistical Mechanics: Entropy, Order Parameters, and Complexity*, Oxford University Press, 2021. Exercise 1.1.

---

## 1. Motivation: Why Dice?

Statistical mechanics is often introduced through the lens of partition functions, entropy, and the canonical ensemble. Yet before we confront the intimidating complexity of $10^{23}$ particles, Sethna invites us to play a game—a game with dice. The brilliance of this exercise lies in its transparency: by mapping quantum statistics onto the familiar act of rolling dice, we can *see* the combinatorial origins of Bose-Einstein and Fermi-Dirac distributions without ever solving a Schrödinger equation.

The premise is disarmingly simple. We have two three-sided dice, each showing 1, 2, or 3 spots. We play three variants of a game:

| Game | Rule | Quantum Analog |
|------|------|----------------|
| **Distinguishable** | All rolls are legal. | Classical distinguishable particles |
| **Bosons** | The second die must show $\geq$ the first. | Bosons: multiple occupancy allowed |
| **Fermions** | The second die must show $>$ the first. | Fermions: Pauli exclusion principle |

The connection to quantum mechanics is profound. Non-interacting identical particles in quantum mechanics are governed by precisely these rules: bosons can occupy the same single-particle state, while fermions cannot. Our dice are merely a discrete, finite-state caricature of this infinite-dimensional truth.

<!-- Image placeholder: Quantum dice table -->
<!-- Place an image file named `fig-quantum-dice-table.png` in the images directory to display the table of allowed rolls for the three games. -->

---

## 2. Part (a): The Probability of Rolling a 5

**Problem:** For a legal turn in each of the three games, what is the probability $\rho(5)$ of rolling a sum of 5?

### Analysis

Let us enumerate the state space systematically. For two three-sided dice, the possible ordered pairs $(n_1, n_2)$ with $n_i \in \{1,2,3\}$ are:

$$
(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)
$$

There are $3 \times 3 = 9$ equally likely outcomes before any quantum filtering is applied.

#### Distinguishable
All 9 outcomes are legal. The pairs summing to 5 are $(2,3)$ and $(3,2)$. Thus:

$$
\rho_{\text{Dist}}(5) = \frac{2}{9}
$$

#### Bosons
Only outcomes with $n_2 \geq n_1$ are permitted. The legal set is:

$$
(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)
$$

There are 6 legal configurations. The pairs summing to 5 are $(2,3)$ only—note that $(3,2)$ is excluded because $2 < 3$. Therefore:

$$
\rho_{\text{Boson}}(5) = \frac{1}{6}
$$

#### Fermions
Only outcomes with $n_2 > n_1$ are permitted. The legal set is:

$$
(1,2), (1,3), (2,3)
$$

There are 3 legal configurations. Only $(2,3)$ sums to 5. Hence:

$$
\rho_{\text{Fermion}}(5) = \frac{1}{3}
$$

### Reflection

It is striking that the Fermion game yields the *highest* probability for rolling a 5, despite having the smallest sample space. This is not a paradox but a lesson in conditional probability: by conditioning on the antisymmetry constraint $n_2 > n_1$, we discard the low-sum outcomes $(1,1), (2,2), (3,3)$ disproportionately, thereby concentrating the remaining probability mass toward larger sums. The boson game, by contrast, includes the diagonal terms, diluting the probability of any specific off-diagonal sum.

---

## 3. Part (b): The Probability of Rolling Doubles

**Problem:** For a legal turn in the three games, what is the probability of rolling a double?

### Solution

#### Distinguishable
Doubles correspond to $(1,1), (2,2), (3,3)$. All three are legal:

$$
P_{\text{Dist}}(\text{double}) = \frac{3}{9} = \frac{1}{3}
$$

#### Bosons
The same three doubles are legal in the boson game:

$$
P_{\text{Boson}}(\text{double}) = \frac{3}{6} = \frac{1}{2}
$$

#### Fermions
By the Pauli exclusion principle encoded in $n_2 > n_1$, no doubles are permitted at all:

$$
P_{\text{Fermion}}(\text{double}) = \frac{0}{3} = 0
$$

### Reflection

This result is the discrete, finite-state avatar of one of the most consequential facts in physics: **fermions cannot occupy the same quantum state**, while **bosons exhibit enhanced probability of clustering in the same state**. The factor of $1/2$ vs. $1/3$ is the germ of Bose-Einstein condensation—the tendency of bosons to pile into the ground state at low temperatures. The zero for fermions is the Pauli exclusion principle, responsible for the stability of matter, the periodic table, and white dwarf stars.

---

## 4. Part (c): Quantum Coins and the Thermodynamic Limit

**Problem:** Now we decrease the dice to $N=2$ sides (a coin, with T and H), and increase the number of coins to $M$. We flip all $M$ coins simultaneously, repeating until a legal sequence occurs. In the coin ordering, $T < H$. What is the probability, in each game, that all $M$ flips are the same (all H or all T)?

### Setup

For $M$ coins, each flip is a sequence of length $M$ over $\{T, H\}$. There are $2^M$ possible sequences before filtering. Because $T < H$, any legal boson sequence must be of the form:

$$
\underbrace{T \cdots T}_{m} \underbrace{H \cdots H}_{M-m}
$$

for some $m \in \{0, 1, \dots, M\}$. There are $M+1$ such legal boson sequences. For fermions, since strict inequality is required, we must have at least one $T$ and at least one $H$ with all $T$'s preceding all $H$'s. Thus $m \in \{1, 2, \dots, M-1\}$, giving $M-1$ legal fermion sequences.

#### Distinguishable
All $2^M$ sequences are legal. Only two sequences are uniform: $T^M$ and $H^M$. Therefore:

$$
P_{\text{Dist}}(\text{uniform}) = \frac{2}{2^M} = 2^{1-M}
$$

#### Bosons
There are $M+1$ legal sequences. The uniform sequences $T^M$ ($m=M$) and $H^M$ ($m=0$) are both legal. Hence:

$$
P_{\text{Boson}}(\text{uniform}) = \frac{2}{M+1}
$$

#### Fermions
There are $M-1$ legal sequences. However, neither $T^M$ nor $H^M$ is legal—fermions require both species to be present. Thus:

$$
P_{\text{Fermion}}(\text{uniform}) = 0
$$

### Reflection: The Approach to the Macroscopic World

As $M \to \infty$, the distinguishable probability decays exponentially as $2^{1-M}$, becoming astronomically small. The boson probability, by contrast, decays only algebraically as $2/(M+1)$. For $M = 10^{23}$, the difference is incomprehensibly vast. This is the essence of **Bose-Einstein condensation**: in a macroscopic system, a non-negligible fraction of bosons can occupy the single-particle ground state, giving rise to superfluidity, lasing, and the peculiar low-temperature behavior of liquid helium-4.

The partition function $Z$ makes its first appearance here. For bosons, the probability of any *specific* legal sequence is enhanced by a factor of $1/Z_{\text{Boson}}$ relative to the raw coin-flip probability, where:

$$
Z_{\text{Boson}} = \frac{M+1}{2^M}
$$

is precisely the probability that a random toss of $M$ coins happens to be legal. This normalization factor—seemingly a mere bookkeeping device—will become the central object of statistical mechanics, encoding all thermodynamic information in a single scalar function.

---

## 5. Part (d): Biased Coins and the Partition Function

**Problem:** Now the coin is biased, with $p = 1/3$ for H and $1-p = 2/3$ for T. (a) What is $p_{TT\cdots T}$ for all tails? What is $Z_{\text{Dist}}$? What is the probability of all tails in Distinguishable? Express the probability of all tails in Bosons in terms of $Z_{\text{Boson}}$. Write $p_{T\cdots TH\cdots H}$ for $M-m$ tails followed by $m$ heads. Sum these to find $Z_{\text{Boson}}$. As $M \to \infty$, what is the probability in Bosons that all coins are tails?

### Solution

#### Raw probabilities before filtering

For $M-m$ tails followed by $m$ heads:

$$
p_{T^{M-m} H^m} = \left(\frac{2}{3}\right)^{M-m} \left(\frac{1}{3}\right)^m = \frac{2^{M-m}}{3^M}
$$

The all-tails sequence has $m=0$:

$$
p_{T^M} = \left(\frac{2}{3}\right)^M = \frac{2^M}{3^M}
$$

#### Distinguishable

Since all $2^M$ sequences are legal:

$$
Z_{\text{Dist}} = \sum_{\alpha} p_\alpha = \sum_{k=0}^{M} \binom{M}{k} \left(\frac{2}{3}\right)^{M-k} \left(\frac{1}{3}\right)^k = \left(\frac{2}{3} + \frac{1}{3}\right)^M = 1
$$

This confirms the normalization of probability. The probability of all tails is simply:

$$
P_{\text{Dist}}(T^M) = p_{T^M} = \left(\frac{2}{3}\right)^M
$$

#### Bosons: The partition function

The legal boson sequences are $T^{M-m} H^m$ for $m = 0, 1, \dots, M$. Each has probability $2^{M-m}/3^M$. Therefore:

$$
Z_{\text{Boson}} = \sum_{m=0}^{M} \frac{2^{M-m}}{3^M} = \frac{1}{3^M} \sum_{m=0}^{M} 2^{M-m} = \frac{1}{3^M} \sum_{k=0}^{M} 2^k = \frac{2^{M+1}-1}{3^M}
$$

The probability of all tails *in a legal boson turn* is the raw probability divided by $Z_{\text{Boson}}$:

$$
P_{\text{Boson}}(T^M) = \frac{p_{T^M}}{Z_{\text{Boson}}} = \frac{2^M / 3^M}{(2^{M+1}-1)/3^M} = \frac{2^M}{2^{M+1}-1}
$$

#### The thermodynamic limit

As $M \to \infty$:

$$
P_{\text{Boson}}(T^M) = \frac{2^M}{2^{M+1}-1} = \frac{1}{2 - 2^{-M}} \xrightarrow{M \to \infty} \frac{1}{2}
$$

This is a remarkable result. Even though the raw probability of all tails decays as $(2/3)^M$, the *conditional* probability—given that the sequence is legal—approaches $1/2$. The boson constraint, by discarding the overwhelmingly numerous but low-probability mixed sequences, actually *enhances* the likelihood of finding the system in its ground state ($T$, the lower-energy state in this biased analogy).

### Physical Interpretation: Bose Condensation

We can interpret the biased coin as a two-level quantum system with $E_T < E_H$. The bias $p = 1/3$ for H reflects the Boltzmann factor: the higher-energy state is less probable, but not forbidden. In the boson game, the requirement that all particles pile into non-decreasing order means that the ground state $T$ is not just favored—it is *macroscopically occupied*.

In the language of many-body physics, this is **Bose-Einstein condensation**: below a critical temperature, a finite fraction of $N$ non-interacting bosons occupies the single-particle ground state. The partition function $Z$, which began here as a humble normalization constant, becomes the gateway to computing free energy, entropy, and all thermodynamic observables. Sethna's dice exercise is, in miniature, the entire story of Chapters 6 and 7 of his book.

---

## 6. Synthesis: From Dice to Many-Body Physics

Let us step back and appreciate the trajectory of this exercise.

We began with two three-sided dice—a toy system with 9 microstates. By imposing simple ordering constraints, we recovered the essential combinatorics of quantum statistics. The fermion constraint ($n_2 > n_1$) enforced the Pauli exclusion principle, yielding zero probability for doubles. The boson constraint ($n_2 \geq n_1$) allowed clustering, enhancing the probability of macroscopic occupancy of a single state.

When we scaled to $M$ coins, the distinction between statistics became quantitative and then dramatic. For distinguishable particles, the probability of uniform occupancy decayed exponentially. For bosons, it decayed only as $1/M$—and in the biased case, the conditional probability of the ground state actually saturated to a finite value. This is the mathematical seed of Bose-Einstein condensation.

The partition function $Z$ emerged organically as the probability of a random configuration satisfying the quantum constraint. In the canonical ensemble, we will learn that:

$$
Z = \sum_\alpha e^{-\beta E_\alpha}
$$

where the sum runs over all many-body states consistent with the symmetry of the particles. For bosons, this sum includes all symmetric states; for fermions, all antisymmetric states. The dice exercise has given us an intuitive preview of why these sums behave so differently—and why the world looks classical at high temperatures, quantum at low temperatures, and superfluid at very low temperatures.

---

## 7. Further Reading

- **Sethna, Ch. 6:** The canonical ensemble and the partition function.
- **Sethna, Ch. 7:** Quantum statistics and Bose-Einstein condensation.
- **Pathria & Beale, Ch. 5:** Ideal Bose and Fermi gases.
- **Landau & Lifshitz, *Statistical Physics I*, §54-57:** The quantum ideal gas.

---

*This note was written as part of a self-study journey through Sethna's textbook. The goal is not merely to solve exercises, but to extract the narrative thread that connects microscopic rules to macroscopic phenomena.*
