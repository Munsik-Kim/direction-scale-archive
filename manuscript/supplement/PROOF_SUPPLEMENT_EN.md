# Direction--Scale: Full English Proof Supplement

Version V2 after a bounded response to separate V1 review; V1 and the original opinion are retained. This supplement reconstructs the frozen STEP06 V2, STEP07, STEP08 and STEP09 derivations in English. It accompanies the unchanged v0.3 manuscript, whose body remains a set of proof sketches. Decimal endpoints are exact rationals. Statements are about the explicitly restricted population model. Scalar computations, numerical observations and agent review are separate evidence; none is formal verification or a novelty certificate.

# S.1 Data law, population risk, and the restricted embedding

Choose the easy or hard group with probabilities $w=1-p$ and $p$. Queries are $q_e=(1,0)$ and $q_h=(0,1)$. Fix $W_K=I_4$. The correct and incorrect keys are respectively $+e_2,-e_2$ in the easy group and $+e_4,-e_4$ in the hard group. The two columns of $W_Q$ are
\[
 w_e=r_e(\cos\phi_e,\sin\phi_e,0,0)^\top,\qquad
 w_h=r_h(0,0,\cos\phi_h,\sin\phi_h)^\top .
\]
Scores are inner products of the normalized column with its unit key, so the correct-minus-incorrect gaps are $g=2\sin\phi_e$, $h=2\sin\phi_h$. A zero coordinate outside a designated column plane has zero loss derivative: the relevant key has zero such coordinate, and the normalization derivative contains that same zero column coordinate. Hence both planes are invariant. The loss gradient is tangent to the column because normalization is homogeneous of degree zero. Fixed keys, one-hot queries and fixed weighted-sum readout are essential to this embedding. No free-QK or arbitrary-query equivalence is asserted.

At test length $M+1$, one correct key and $M$ copies of the incorrect key have independent Rademacher values $V_0,\ldots,V_M$. The values are independent of query, keys and learned scores. For an absolute evaluation scale $b\ge0$, the correct attention weight is $e^{bd}/(e^{bd}+M)$ and each incorrect weight is $1/(e^{bd}+M)$. The predictor is the weighted sum of the values and the target is the correct value. Therefore
\[
 f-V_0=(A_0-1)V_0+\sum_{j=1}^M A_jV_j,\qquad
 \mathbb E[(f-V_0)^2]=(1-A_0)^2+\sum_{j=1}^M A_j^2
 =\ell_M(bd)=\frac{M(M+1)}{(e^{bd}+M)^2}.
\]
The cross terms vanish by independence and zero means; every diagonal second moment is one. Repeating a key does not repeat a value. Joint permutation of positions and the designated target preserves this identity. One-hot attention at any location returns that location's value exactly.

Training uses $M=1$, the direct scale $\beta$, and population loss without a factor $1/2$:
\[
 \ell(z)=\frac{2}{(1+e^z)^2},\qquad K(z)=-\ell'(z)=\frac{4e^z}{(1+e^z)^3},
 \qquad J=w\ell(\beta g)+p\ell(\beta h).
\]
For every group, $\partial_{\phi_i}J=-2p_i\beta\cos\phi_iK(\beta d_i)$ and $\partial_\beta J=-\sum_i p_i d_iK(\beta d_i)$. Cartesian direction GF of rate $\rho$ and direct beta GF of rate one consequently give
\[
 \dot\beta=wgK(\beta g)+phK(\beta h),\qquad
 \dot\phi_i=\frac{2\rho p_i\beta\cos\phi_iK(\beta d_i)}{r_i^2},
 \quad p_e=w,\ p_h=p .
\]
Tangency proves that GF radii are constant in time, but they vary with initialization. The beta equation is projected only at zero. Hold fixes the same instance's initial $\beta_0$; it does not replace all initial scales by one.

Throughout the box result,
\[
 \xi=(p,\beta_0,r_e,r_h,g_0,\theta_h)\in
 K_0=[.049,.051]\times[.99,1.01]\times[.95,1.05]^2
       \times[.19,.21]\times[.79,.81],
\]
with $\phi_{e0}=\arcsin(g_0/2)$, $\phi_{h0}=-\theta_h$, $a_0=2\sin\theta_h$. This initialization is independent of $\rho$. Define $T_0=\inf\{t:h_J(t)\ge0\}$, with empty infimum infinity, and $B_\rho=\sup_{0\le t\le T_0}\beta(t)$. Finite correction and supremum attainment are not assumed before being proved.

# S.2 Global GF, beta floor, invariant and general-radii coordinates

Use the common constants
\[
\begin{gathered}
 p_-=.049,\ p_+=.051,\ w_-=.949,\ w_+=.951,\quad
 \beta_-=.99,\ \beta_+=1.01,\ r_-=.95,\ r_+=1.05,\\
 g_-=.19,\ g_+=.21,\ a_-=1.42,\ a_+=1.45 .
\end{gathered}
\]
Alternating sine/cosine series and positive exponential series with rational remainders, specified in S.10, give $a_-<a_0<a_+$, $\cos\theta_h>.68$, $\arcsin(.1)<.101$, $e^{-.99}<.372$, $e^{-.1881}<.829$. In particular $a_0-2g_0>1$ uniformly.

Differentiating $K$ gives $K'=K(1-3e^z/(1+e^z))$. With $x=e^z>0$, $4x/(1+x)^3$ has one maximum at $x=1/2$. Thus
\[
 0<K\le16/27,\quad |K'|\le32/27,\quad |(\log K)'|\le2.
\]
For $z\ge0$, $\frac12e^{-2z}\le K(z)\le4e^{-2z}$; for $u\ge0$, $\frac12e^{-u}\le K(-u)\le4e^{-u}$. These follow by writing the denominator as $(1+e^{-z})^3$, between one and eight.

**Global existence and positive floor.** On an interior chart with positive beta, the vector field is smooth. On a sufficiently small closed ball, let its bound be $A$ and its Lipschitz constant $L$. Choosing a time interval with $A\Delta t$ below the ball's margin and $L\Delta t<1$, iteration of the integral map is a contraction on continuous curves. Its limit is a differentiable solution and the same inequality proves uniqueness.

As long as beta is positive, both angles and hence both gaps increase. At $\beta=.01$, the mean-value bound on $K$, $K(0)=1/2$, and $\sum_i p_i d_i^2\le4$ imply
\[
 \dot\beta\ge\tfrac12(w_-g_--p_+a_+)-128/2700
       =7793/1350000>0 .
\]
An initially positive solution cannot first cross below this level with a positive derivative. Hence $\beta\ge.01$; zero projection is inactive. Also $|\dot\beta|\le32/27$, giving $\beta(t)\le\beta_++32t/27$ on every finite interval. Let $Y_i=\operatorname{atanh}(\sin\phi_i)$. Its derivative is
\[
 \dot Y_i=2\rho p_i\beta K(\beta d_i)/r_i^2 .
\]
It is nonnegative and integrably bounded on any finite interval. Thus neither $Y_i=-\infty$ nor $Y_i=+\infty$ is reached in finite time. The angles remain in a compact interior part of the principal chart. The field and its derivative are bounded on the resulting finite-time compact domain; the solution has an interior limit at a hypothetical finite maximal time, where the local integral construction extends it. This contradiction proves unique global finite-time existence, independently of correction. Hold is identical in this argument with fixed positive beta.

**Conservation and its domain.** Direct differentiation cancels the scale and angle forces:
\[
 Q=\rho\beta^2/2+r_e^2\log\cos\phi_e+r_h^2\log\cos\phi_h,\qquad \dot Q=0 .
\]
Before correction put $u=\sqrt\rho\beta$ and $D_h=\log\cos\phi_h-\log\cos\phi_{h0}\ge0$. Then
\[
 \cos^2\phi_e=A_\xi e^{(\rho\beta_0^2-u^2)/r_e^2}
                e^{-2(r_h^2/r_e^2)D_h},\qquad A_\xi=1-g_0^2/4.
\]
Define
\[
 G_{\rho,\xi}(u)=2\sqrt{1-A_\xi e^{(\rho\beta_0^2-u^2)/r_e^2}},
 \qquad G_\xi(u)=2\sqrt{1-A_\xi e^{-u^2/r_e^2}}.
\]
We use $g\ge G_{\rho,\xi}(u)\ge g_0$ only when $u\ge\sqrt\rho\beta_0$. The exact initial term is retained. No square root outside its stated domain is taken.

Let $H_\xi=1-a_0^2/16$. Then
\[
 b_\xi=r_e\sqrt{\log(A_\xi/H_\xi)},\qquad c_\xi=a_0b_\xi,
 \qquad G_\xi(b_\xi)=a_0/2.
\]
Common bounds are
\[
 A_{\min}=.988975,\ A_{\max}=.990975,\quad
 H_{\min}=.86859375,\ H_{\max}=.873975.
\]
For $x>1$, integration of $1/t$ gives $1-1/x\le\log x\le x-1$. The exact comparisons
\[
 r_-^2(1-H_{\max}/A_{\min})>.32^2,\qquad
 r_+^2(A_{\max}/H_{\min}-1)<.4^2
\]
therefore give $b_-:=.32<b_\xi<b_+:=.4$, and $c_\xi>c_-:=.4544$. Define also $R_*:=r_+^2/r_-^2=441/361$ and $T_*:=1/.68=25/17$; these bound the squared-radius ratio and the pre-correction hard tangent.

# S.3 Uniform live entry, outer first hit and actual-clock lower bounds

This section constructs common constants. Uniformity is not deduced from pointwise limits and compactness.

**Frozen ratio and live entry.** At the initial angles, for every $\beta\ge\beta_0$,
\[
 R_0(\beta;\xi)=\frac{pa_0}{wg_0}e^{-(a_0-2g_0)\beta}
       \left(\frac{1+e^{-g_0\beta}}{1+e^{-a_0\beta}}\right)^3
 \le U_K:=\frac{841573862939583}{901550000000000}<.94 .
\]
Indeed drop the denominator, bound its remaining prefactor by $p_+a_+/(w_-g_-)$, and use $a_0-2g_0>1$, $\beta\ge.99$, $g_0\beta\ge.1881$ with the enclosures in S.2. This frozen statement alone does not establish a live trajectory bound.

Fix $0<\lambda<1$ before choosing $\rho$, and put $\bar u_\xi=(1-\lambda)b_\xi$, $\bar u_-=(1-\lambda)b_-$. The squared-gap identity and $e^x-1\ge x$ yield
\[
 a_0-2G_\xi(\bar u_\xi)\ge
 m_\lambda:=\frac{8H_{\min}b_-^2(2\lambda-\lambda^2)}{r_+^2a_+}>0 .
\]
To see the denominator direction, divide the squared gap difference by $a_0/2+G_\xi(\bar u_\xi)\le a_+$. If hard angle displacement is at most $\delta$ and $u\le\bar u_\xi$, conservation bounds
\[
 g\le G_{\delta,\xi}:=
 2\sqrt{1-A_\xi e^{-\bar u_\xi^2/r_e^2-2R_*T_*\delta}},
 \qquad G_{\delta,\xi}-G_\xi(\bar u_\xi)\le4R_*T_*\delta/g_- .
\]
Here $D_h\le T_*\delta$, and dropping the positive initial beta term makes an upper gap estimate. The square-root difference is controlled by integrating its derivative on the domain where the gap is at least $g_-$.

Set
\[
 L_\delta=2+8R_*T_*/g_-,\quad
 \delta_\lambda=\min(.79/2,a_-/4,m_\lambda/(2L_\delta)),\quad
 \kappa_\lambda=m_\lambda/2,\quad a_{\min}=a_--2\delta_\lambda\ge a_-/2 .
\]
On this tube, $a=-h\ge a_{\min}$ and $a-2g\ge\kappa_\lambda$. Define
\[
 C_R=8p_+a_+/(w_-g_-),\quad
 B_0=\max(\beta_++1,\log(2C_R)/\kappa_\lambda+1),\quad q=.97,
\]
\[
 \sigma=\min\left(\delta_\lambda/2,g_-/4,a_-/4,.01,
 \frac{\log(q/.94)}{2(2/a_-+2/g_-+4B_0)}\right)>0 .
\]
For $\beta_0\le\beta\le B_0$ and each angle displacement at most $\sigma$, the log force ratio changes from its frozen value by at most $2\sigma(2/a_-+2/g_-+4B_0)$. This follows by integrating the derivatives of log gaps and log kernels, using gap change at most $2\sigma$ and $|(\log K)'|\le2$. The log-gap denominators remain positive since the choices of $\sigma$ keep them above half their initial lower bounds. Thus the live ratio is at most $q<1$.

On that entry box define
\[
 m_{\rm ent}=\frac{(1-q)w_-g_-}{4}e^{-2B_0(g_++2\sigma)},\quad
 \tau_{\rm ent}=(B_0-\beta_-)/m_{\rm ent},\quad
 A_{\rm ent}=32B_0/(27r_-^2),\quad C_{\rm init}=A_{\rm ent}\tau_{\rm ent}.
\]
The kernel lower bound gives $\dot\beta\ge m_{\rm ent}>0$, and each angle speed is at most $\rho A_{\rm ent}$. If $\rho A_{\rm ent}\tau_{\rm ent}<\sigma$, no angle can first exit before beta reaches $B_0$ within $\tau_{\rm ent}$. A downward beta exit is excluded by its positive derivative. All constants are common across the varying initial $\beta_0$. This is a finite-entry argument, not continuous dependence over an exponentially long interval.

**Outer bootstrap and finite first hit.** After entry, while $u\le\bar u_\xi$ and the hard tube holds,
\[
 R\le C_R e^{-\kappa_\lambda\beta}\le1/2,\qquad
 \frac{d\phi_h}{d\beta}\le
 \frac{4\rho C_R}{r_-^2a_{\min}}\beta e^{-\kappa_\lambda\beta}.
\]
The first inequality follows from the exact kernel ratio with numerator factor at most eight. The second retains the true hard-radius denominator and divides only by the positive scale force. Integrating the exponential tail, including the entry displacement, gives hard angle movement at most $\rho C_h$, where
\[
 C_h=C_{\rm init}+\frac{4C_R}{r_-^2a_{\min}}
 e^{-\kappa_\lambda B_0}(B_0/\kappa_\lambda+1/\kappa_\lambda^2).
\]
Take
\[
 \rho_{\rm out}(\lambda)=\min\left(1,
 \frac{\sigma}{A_{\rm ent}\tau_{\rm ent}},
 \frac{\delta_\lambda}{C_h},(\bar u_-/B_0)^2\right)>0 .
\]
For $0<\rho<\rho_{\rm out}$, a first hard-tube exit contradicts the strict displacement bound, and entry precedes the desired scale level. On the remaining finite beta interval, the positive scale force has a positive lower bound. Global continuation therefore forces a finite first hit of $u=\bar u_\xi$ before hard correction. No later ascent is assumed to remain in this tube.

Up to that first hit, with $V=\beta_+^2/r_-^2$,
\[
 |g-G_\xi(u)|\le C_g\rho,\qquad
 C_g=4R_*T_*C_h/g_-+2Ve^V/g_- .
\]
The first term controls hard log-cos motion, and the second controls the initial term through $e^{\rho\beta_0^2/r_e^2}-1\le\rho Ve^V$. These estimates retain both initial beta and general-radii factors.

**Physical-clock sandwich.** Put $F_\xi(u)=2uG_\xi(u)$. It is increasing, and on $0\le u\le b_+$,
\[
 |F_\xi'(u)|\le L_F:=4+8b_+^2/(r_-^2g_-).
\]
The force ratio estimates on entry and outer portions give
\[
 k_-e^{-2\beta g}\le\dot\beta\le k_+e^{-2\beta g},\qquad
 k_-=(1-q)w_-g_-/2,\quad k_+=8 .
\]
Changing the actual clock via $u=\sqrt\rho\beta$ and using the gap error yields, for the first-hit time $\bar t_\xi$,
\[
 \frac1{k_+\sqrt\rho}\int_{\sqrt\rho\beta_0}^{\bar u_\xi}
 e^{F_\xi(u)/\sqrt\rho-2b_+C_g\sqrt\rho}\,du
 \le\bar t_\xi\le
 \frac1{k_-\sqrt\rho}\int_{\sqrt\rho\beta_0}^{\bar u_\xi}
 e^{F_\xi(u)/\sqrt\rho+2b_+C_g\sqrt\rho}\,du .
\]
Fix a common $0<d\le\bar u_-/4$ and impose $\rho<(\bar u_-/(2\beta_+))^2$. The final length-$d$ integration interval is then inside every integration domain. There $F_\xi\ge F_\xi(\bar u_\xi)-L_Fd$; on the whole domain its maximum is $F_\xi(\bar u_\xi)$ and the length is at most $b_+$. Taking logarithms of these explicit bounds gives
\[
 F_\xi(\bar u_\xi)-L_Fd-\omega(\rho)
 \le\sqrt\rho\log(1+\bar t_\xi)\le F_\xi(\bar u_\xi)+\omega(\rho),
\]
\[
 \omega(\rho)\le H_\lambda\rho+A_d\sqrt\rho+2\rho^{1/4},\quad
 H_\lambda=2b_+C_g,\quad
 A_d=\max(|\log(d/k_+)|,\log(1+b_+/k_-)).
\]
The estimate $\frac12\sqrt\rho\log(1/\rho)\le2\rho^{1/4}$ follows by integrating $1/t$ or differentiating the corresponding elementary bound. For the upper inequality, bound $1+\bar t$ directly; no unknown divergence is used. For the lower inequality use $\log(1+\bar t)\ge\log\bar t$.

**Uniform time and peak lower statements.** Because $F_\xi(b_\xi)=c_\xi$ and $c_\xi-F_\xi(\bar u_\xi)\le L_F\lambda b_+$, for a prescribed $\varepsilon>0$ choose, in order,
\[
 \lambda=\min(1/2,\varepsilon/(3L_Fb_+)),\qquad
 d=\min((1-\lambda)b_-/4,\varepsilon/(3L_F)).
\]
Construct all entry/tube constants at this fixed lambda and only then choose
\[
 \rho_{\rm LB}(\varepsilon)=\min\left(
 \rho_{\rm out}(\lambda),(\bar u_-/(2\beta_+))^2,
 \varepsilon/(9H_\lambda),[\varepsilon/(9(A_d+1))]^2,
 (\varepsilon/18)^4\right)>0 .
\]
Then for every $\xi\in K_0$ and $0<\rho<\rho_{\rm LB}$,
$\sqrt\rho\log(1+T_0)\ge c_\xi-\varepsilon$, since the first hit precedes $T_0$. This argument remains meaningful if $T_0$ is still allowed to be infinite, and uses no upper theorem.

For the distinct peak lower bound choose $\lambda_P=\min(1/2,\varepsilon/b_+)$, then $\rho<\rho_{\rm out}(\lambda_P)$. At its first hit, $u=(1-\lambda_P)b_\xi$, so $\sqrt\rho B_\rho\ge b_\xi-\varepsilon$. Both limits fix the buffer before taking $\rho$ small.

# S.4 Uniform positive variation, finite correction, and sharp upper limits

The buffer is denoted $\nu>0$ to distinguish it from the GD step $\eta$. Fix it before $\rho$ and set $v_\xi=b_\xi+\nu/2$. Define
\[
 \Delta_\nu=b_-\nu/r_+^2,\quad
 m_\nu^+=\frac{8H_{\min}}3\frac{\Delta_\nu}{1+\Delta_\nu},\quad
 \kappa_\nu=m_\nu^+/2 .
\]
Indeed
\[
 G_\xi(v_\xi)^2-(a_0/2)^2=4H_\xi(1-e^{-\Delta_\xi}),
 \quad\Delta_\xi=(v_\xi^2-b_\xi^2)/r_e^2\ge\Delta_\nu .
\]
Use $1-e^{-x}\ge x/(1+x)$ and $G_\xi(v_\xi)+a_0/2<3$ to get $2G_\xi(v_\xi)-a_0\ge m_\nu^+$. With $C_0=2Ve^V/g_-$, impose
\[
 \rho_{\rm U1}(\nu)=\min(1,(b_-/\beta_+)^2,m_\nu^+/(4C_0)).
\]
For $0<\rho<\rho_{\rm U1}$, $v_\xi>\sqrt\rho\beta_0$ and $2G_{\rho,\xi}(v_\xi)-a_0\ge\kappa_\nu$. Consequently, at every pre-correction time with $u\ge v_\xi$, conservation gives $2g-a\ge\kappa_\nu$. This uses neither the lower tube nor live entry.

The hard progress is strictly positive:
\[
 -\dot a=\rho p\beta(4-a^2)K(-\beta a)/r_h^2>0 .
\]
Discarding the negative hard term in the scale force and using the exact kernel ratio gives
\[
 \frac{(\dot u)_+}{-\dot a}
 \le\frac{16wr_h^2}{p(4-a_0^2)u}
             e^{-(2g-a)u/\sqrt\rho}
 \le D_K e^{-\kappa_\nu b_-/\sqrt\rho},\quad
 D_K=\frac{16w_+r_+^2}{p_-(4-a_+^2)b_-}.
\]
This comparison divides by hard progress, never by $\dot\beta$ at a turning point. Let $E(t)=(u(t)-v_\xi)_+$. On any finite interval, $u$ is $C^1$ and $E$ is absolutely continuous. At level-set points with nonzero derivative the level crossing is isolated; these points form a countable set. At level-set points with zero derivative, $E'=0$. Thus $E'=\mathbf1_{\{u>v_\xi\}}\dot u$ almost everywhere. Since $E(0)=0$,
\[
 E(t)\le\int_0^t\mathbf1_{\{u>v_\xi\}}(\dot u)_+\,ds
 \le A_K e^{-\kappa_\nu b_-/\sqrt\rho},\qquad A_K=a_+D_K,\quad t<T_0.
\]
The total hard decrease is at most $a_0\le a_+$; all excursions, reentries and repeated positive scale variations use this single budget. Finite correction, a first-peak/global-peak identity, a bound on the number of turns, or $\beta(T_0)=O(1)$ has not been assumed.

Now choose
\[
 \rho_{\rm cap}(\nu)=\min\left(\rho_{\rm U1}(\nu),
 [\kappa_\nu b_-/\log(1+2A_K/\nu)]^2\right)>0 .
\]
For $0<\rho<\rho_{\rm cap}$, the excess is strictly below $\nu/2$, giving $u(t)\le b_\xi+\nu$ at every pre-correction time. The bound retains each individual $b_\xi$, not merely its maximum over the box.

**Finite correction, without circularity.** Combine the cap with $\beta\ge.01$, $a\le a_0$ and $K(-\beta a)\ge\frac12e^{-\beta a}$:
\[
 -\dot a\ge k_{H,K}\rho e^{-a_0(b_\xi+\nu)/\sqrt\rho},
 \quad k_{H,K}=\frac{p_-\cdot.01(4-a_+^2)}{2r_+^2}>0 .
\]
The right side is a positive constant in physical time. If correction had not occurred by $a_+$ divided by that speed, integrating it would force $a\le0$, a contradiction. Global existence was already proved independently. Hence
\[
 T_0\le C_K\rho^{-1}e^{(c_\xi+a_0\nu)/\sqrt\rho}<\infty,\qquad C_K=a_+/k_{H,K}.
\]
One common existence cutoff is $\rho_K=\rho_{\rm cap}(1)$. Continuity extends the cap to the finite endpoint. At $h=0$, $\dot h=2\rho p\beta/r_h^2>0$, so the event is a crossing.

For any prescribed $\varepsilon>0$, first choose $\nu=\varepsilon/a_+$ and then $\rho<\rho_{\rm cap}(\nu)$. The time bound has exponent at most $(c_\xi+\varepsilon)/\sqrt\rho$, a common prefactor $C_K$ and power $\rho^{-1}$. This does not prove a limiting prefactor.

For the normalized uniform time upper limit use $\nu=\varepsilon/(2a_+)$ and $B_c=\log(1+C_K)$. Since
\[
 \sqrt\rho\log(1+C_K/\rho)\le B_c\sqrt\rho+4\rho^{1/4},
\]
the common choice
\[
 \rho_{\rm timeUB}(\varepsilon)=\min\left(
 \rho_{\rm cap}(\varepsilon/(2a_+)),
 [\varepsilon/(4(B_c+1))]^2,(\varepsilon/16)^4\right)
\]
gives $\sqrt\rho\log(1+T_0)\le c_\xi+\varepsilon$. The cap with buffer $\nu=\varepsilon$ gives the peak upper bound $u\le b_\xi+\varepsilon$. Intersect the relevant common upper and lower cutoffs, and the finite-existence cutoff if needed. For every $\varepsilon>0$ the resulting cutoff works simultaneously for all $\xi$. Therefore
\[
 \lim_{\rho\downarrow0}\sup_{\xi\in K_0}
 |\sqrt\rho\log(1+T_0)-c_\xi|=0,\qquad
 \lim_{\rho\downarrow0}\sup_{\xi\in K_0}|\sqrt\rho B_\rho-b_\xi|=0 .
\]
The lower proof uses no upper theorem; positive variation uses no correction finiteness; global existence plus the cap establishes finiteness and the upper theorem. This dependency order excludes circularity.

The common positive lower coefficient also forces T0 to diverge uniformly: below a common cutoff, log(1+T0) is at least c_-/[2 sqrt(rho)]. Thus sqrt(rho)[log(1+T0)-log T0] tends to zero uniformly. The manuscript's exponential reformulation T0=exp[(c_xi+o_K0(1))/sqrt(rho)] follows. It does not assert convergence of T0 divided by the bare exponential, which would require control of an unnormalized remainder.

# S.5 Hold correction, persistence, and all-M GF risk

In slow time $\zeta=\rho t$, Hold has
\[
 \frac{d\phi_i}{d\zeta}=2p_i\beta_0\cos\phi_i K(2\beta_0\sin\phi_i)/r_i^2>0 .
\]
Its global chart proof is the fixed-beta version of S.2. Until the hard target $\gamma=.2$ is attained, $\phi_h\in[-\theta_h,\arcsin(.1)]$ and $\beta_0h\in[-1.4645,.202]$. Exact exponential enclosures are
\[
 .23<e^{-1.4645}<.24,\qquad 1.22<e^{.202}<1.224.
\]
As a function of $e^z$, $K$ increases to one maximum and then decreases. Its minimum on this interval lies at an endpoint. The rational endpoint estimates imply $K>.4$ throughout. Also $\cos\phi_h>.68$ and angle length is less than $.81+.101=.911$. Thus
\[
 \rho T_{\gamma,h}^{H}<
 \frac{.911(1.05)^2}{2(.049)(.99)(.68)(.4)}
 =113875/2992<40 .
\]
A strictly positive pre-hit speed and global existence force the finite hit. If $g_0\ge.2$, the easy hit is time zero. Otherwise its angle length is at most $.005/.99<.006$, its cosine exceeds $.99$, and $K>.4$ on its smaller exponent interval. Consequently
\[
 \rho T_{\gamma,e}^{H}<
 \frac{.006(1.05)^2}{2(.949)(.99)^2(.4)}<.00890<40 .
\]
The maximum of these hit times is below $40/\rho$. Positive chart-angle speeds imply persistence of both gaps for every later finite time. The correct instance-specific $\beta_0$ has been used.

The risk result uses only the lower GF theorem. Fix $\varepsilon=c_-/2$ first. Below $\rho_{\rm LB}(c_-/2)$,
$\sqrt\rho\log(1+T_0^J)\ge c_-/2$. A positive partial series for $e^4$ gives $\log41<4$, and for $\rho\le1$,
\[
 \sqrt\rho\log(1+40/\rho)\le4\sqrt\rho+4\rho^{1/4}.
\]
Thus
\[
 \rho_0=\min(\rho_{\rm LB}(c_-/2),(c_-/32)^4)>0
\]
makes that clock strictly smaller than $c_-/2$. Hence $T_0^J>40/\rho$. At the common time $t_*=40/\rho$, Joint has $h_J<0$ while Hold has both gaps at least $\gamma$.

For every $b\ge0$ and every integer $M\ge1$, $e^{bh_J}\le1$ gives $\ell_M(bh_J)\ge M/(M+1)$. Dropping the nonnegative easy term yields
\[
 \inf_{b\ge0}R_M^J(t_*;b,\xi)\ge p_\xi M/(M+1).
\]
This includes $b=0$ directly and hence also the older $b>0$ formulation. Set
\[
 b_M^K=\frac{\log(4M(M+1)/p_-)}{2\gamma}.
\]
For either Hold gap $d\ge\gamma$,
$\ell_M(b_M^Kd)\le M(M+1)e^{-2b_M^K\gamma}=p_-/4$. Weights sum to one, so
\[
 R_M^H(t_*;b_M^K,\xi)\le p_-/4,\qquad
 \inf_{b\ge0}R_M^J-R_M^H(t_*;b_M^K,\xi)\ge p_-/4=49/4000.
\]
The order is: there exists one $\rho_0$ depending on $K_0,\gamma,40$, then all $\xi\in K_0$, all $0<\rho<\rho_0$, and all integer $M\ge1$. The cutoff is independent of test length; the finite evaluation scale depends on $M$ but is common across arms and $\xi$. Infimum attainment and a numerical scale grid are unnecessary. The sharp upper theorem is not a dependency of this corollary.

**STEP06 base result preserved.** At $\xi_{\rm base}=(.05,1,1,1,.2,.8)$, the sharp GF law specializes with $b_*=.35729699340108\ldots$ and $c_*=.51261834895270\ldots$, merely displayed values of the exact formula. The earlier independent Hold proof uses $1.43<a_0<1.44$, $\cos(.8)>.69$, $\arcsin(.1)<.101$, travel length below $.901$ and $K>.4$ on $[-a_0,.2]$. Hence
\[
 T_\gamma^H<4505/(138\rho)<40/\rho.
\]
The positive time lower coefficient, independently of the upper theorem, gives $T_0^J>40/\rho$ below a base cutoff independent of $M$. Using the base's own scale
\[
 b_M^{\rm base}=\frac{\log(4M(M+1)/(.05))}{.4}
\]
gives Hold risk at most $.05/4$ and difference at least $1/80=.0125$. It is not silently replaced by the box's $49/4000$ rule.

These are population MSE statements for fresh values and fixed query groups. They imply neither accuracy percentage-point improvements, arbitrary-query generalization, one scale for all infinite lengths, nor universal raw Hold superiority.

# S.6 Exact Cartesian GD gradients, chart and changing radii

Both gradients in a step are evaluated at the same pre-node. Directions use $\alpha=\rho\eta$ and Joint uses
\[
 w_{i,+}=w_i-\alpha\nabla_{w_i}J,\qquad
 \beta_+=\max(0,\beta+\eta F),\quad F=wgK(\beta g)+phK(\beta h).
\]
Hold instead keeps the exact initial $\beta_0$. For a column plane, $d=2Y/r$, $s=r^2=X^2+Y^2$:
\[
 \nabla d=(-2XY/r^3,2X^2/r^3),\qquad w\cdot\nabla d=0 .
\]
The negative group gradient is $p_i\beta K(\beta d_i)\nabla d_i$. Put
\[
 D_i=2p_i\beta\cos\phi_iK(\beta d_i),\quad x_i=\alpha D_i/s_i.
\]
The Cartesian tangent step is $r_i(e_{\phi_i}+x_i\tau_i)$, with $\tau_i=(-\sin\phi_i,\cos\phi_i)$. Therefore, exactly,
\[
 s_{i,+}=s_i(1+x_i^2),\qquad \phi_{i,+}=\phi_i+\arctan x_i,
 \qquad \Delta s_i=\alpha^2\|\nabla_{w_i}J\|^2 .
\]
The first coordinate satisfies
\[
 X_{i,+}=X_i[1-\alpha p_i\beta d_iK(\beta d_i)/s_i].
\]
For $z\ge0$, $zK(z)\le4ze^{-2z}\le2$, and for $z<0$ the subtracted quantity is negative. Initially $X_i>0$, $s_i\ge s_-=(19/20)^2$; radii never decrease. For $\alpha\le1/5000$ the factor is at least $1-2\alpha/s_->0$. Projection preserves beta nonnegativity, and $|\eta F|\le\eta32/27$ ensures finite beta at every finite node. Induction proves well-defined finite steps, $X_i>0$, the principal chart, and nondecreasing angles independently of the stopped region. Positive fixed beta makes Hold's increments strictly positive.

No GF invariant is conserved here. Radius reset, replacing $\arctan x$ by $x$, beta-first evaluation, a new positive beta clamp, or log-beta training changes the algorithm. The exact polar identities are proof tools for Cartesian GD.

# S.7 Direct small-rho first exit and the closed cutoff refinement

Set $\delta=.001$, $q=.97$, $\bar\eta=.2$, $c=.38$. On the initial angular tube $0\le\phi_i-\phi_{i0}\le\delta$, monotonicity and $2$-Lipschitz gaps imply
\[
 .19\le g\le.212,\quad1.418\le a=-h\le1.45,\quad a-2g\ge.994 .
\]
For $\beta\ge\beta_0\ge.99$, the exact force ratio obeys
\[
 R=\frac{paK(-\beta a)}{wgK(\beta g)}
 \le\frac{.051\cdot1.45}{.949\cdot.19}
 e^{-.994\cdot.99}(1+e^{-.19\cdot.99})^3<.94<q .
\]
This new tube ratio is not the unchanged frozen GF ratio. The enclosing arithmetic is in S.10. At an in-tube pre-node, $F=F_E(1-R)>0$; simultaneous induction therefore gives an increasing beta and inactive projection.

Before and including a hypothetical first exiting step,
\[
 0<F\le8e^{-c\beta},\quad F\le32/27,\quad
 e^{c\beta_{k+1}}-e^{c\beta_k}
 \le8c e^{c\bar\eta32/27}\eta=A_{\rm GD}\eta .
\]
The inequality follows from $e^x-1\le xe^x$ with $x=c\eta F$. For $N=\lceil40/(\rho\eta)\rceil$ the actual clock has
\[
 40/\rho\le N\eta<40/\rho+\eta .
\]
Summing to any $n\le N$ whose earlier pre-nodes are in the tube gives
\[
 \beta_n\le B_{\rm env}(\rho)=
 c^{-1}\log[e^{c\beta_+}+A_{\rm GD}(40/\rho+\bar\eta)]
 \le c^{-1}[5+\log(1/\rho)]\quad(\rho\le1).
\]
The last bound follows from exact enclosures $A_{\rm GD}<3.4$ and
$e^{c\beta_+}+A_{\rm GD}(40+\bar\eta)<e^5$.

Using $\arctan x\le x$, the actual radius lower bound, and the same pre-state $\Delta\beta=\eta F$,
\[
 \Delta\phi_e\le C_e\rho\beta\Delta\beta,\quad
 \Delta\phi_h\le C_h\rho\beta\Delta\beta,
\quad C_e=\frac{2}{s_-.19(1-q)}=\frac{8000000}{20577},
\quad C_h=\frac{2q}{s_-1.418(1-q)}=\frac{38800000}{767847}<C_e .
\]
For a candidate first exiting post-node $n\le N$, every preceding pre-node is admissible. The complete exiting step is included in the exact identity
\[
 \sum_{k<n}\beta_k\Delta\beta_k
 =\tfrac12[\beta_n^2-\beta_0^2-\sum_{k<n}(\Delta\beta_k)^2]
 \le B_{\rm env}(\rho)^2/2 .
\]
Thus displacement to that post-node is at most
$[C_e/(2c^2)]\rho[5+\log(1/\rho)]^2$.

**Original registered strict condition.** For $\rho\le1$,
$\log(1/\rho)\le4\rho^{-1/4}$, so
$\rho B_{\rm env}^2\le c^{-2}(50\rho+32\sqrt\rho)\le82c^{-2}\sqrt\rho$.
The original condition is
\[
 0<\rho<(\delta c^2/(41C_e))^2
 =\frac{55179596320209}{672400000000000000000000000000}
 \simeq8.20636\,10^{-17}.
\]
It remains a separately identified historical sufficient condition.

**Closed STEP09 addendum.** Let $f(\rho)=\rho[5+\log(1/\rho)]^2$. Its derivative is
$f'=(5+\log(1/\rho))(3+\log(1/\rho))>0$ on $(0,1]$. The exact positive sum $\sum_{j=0}^9(7/3)^j/j!>10$ gives $\log10<7/3$. Therefore for every $0<\rho\le10^{-9}$,
\[
 \frac{C_e}{2c^2}f(\rho)
 \le\frac{C_e}{2c^2}10^{-9}(5+9\log10)^2
 <\frac{C_e}{2c^2}10^{-9}26^2
 =\frac{6760}{7428297}<.001 .
\]
The displacement is strict even at the closed upper endpoint. A first exit is impossible, so the tube, beta increase, inactive projection and $h_{J,k}<0$ hold at every $0\le k\le N$. This proof is for the polynomial horizon $N$ and does not assert a GD sharp exponential escape law. The independent GD Hold proof in S.9 applies because $\rho\le10^{-9}$ is within its $\rho\le.001$ domain.

# S.8 Fixed-anchor asymmetric first exit over the entire closed box

Fix exactly $\rho=1/10000$, $\eta=1/5$, $\alpha=1/50000$,
$N=2000000$, $N\eta=400000$, $N\alpha=40$. There is no parameter partition, rounded-state initialization or numerical trajectory premise.

Set
\[
 g_-=.19,\quad G=.6,\quad a_- =1.38,\quad a_+=1.45,\quad
 B=20,\quad d_{\max}=\eta32/27=32/135.
\]
The closed candidate region at a pre-node is
g0<=g<=G, 0<=phi_h-phi_h0<=.02, beta0<=beta<=B.
Here a=-h lies in [a_-,a_+]: exact alternating sine enclosures give
2sin(.77)>1.38 and 2sin(.81)<1.45. The initial node is strictly inside
all upper barriers for every xi in K0. Let n<=N be a hypothetical first
post-node leaving an upper barrier. Every pre-node k<n is in this region.
The proof below controls this full exiting step, without assuming the
post-node is already inside.

## S.8.1 Continuous-domain force ratio and simultaneous beta induction

Let F_E=(1-p)gK(beta g), F_H=p aK(-beta a), R=F_H/F_E.
For beta>=.99 and a>=1.38, K(-beta a) decreases as beta a increases:
beta a>=1.3662>log2. Thus F_H<=.051*1.45*K(-1.38 beta).

The function g K(beta g) has its minimum on [.19,.6] at an endpoint.
Indeed for z>0,
\[
 \frac{d}{dz}\log[zK(z)]=\frac1z+\frac{1-2e^z}{1+e^z}
\]
is strictly decreasing, with limits of opposite signs. This function
therefore has one maximum; it has no interior minimum.

For v=.19 or .6 define the exact upper ratio
\[
 \mathcal R_v(b)=\frac{.051\,1.45}{.949\,v}
 e^{-(1.38-2v)b}\frac{(1+e^{-vb})^3}{(1+e^{-1.38b})^3}.
\]
Then $R\le\max(\mathcal R_{.19}(\beta),\mathcal R_{.6}(\beta))$.
For v=.19, kappa=1.38-2v=1 and
\[
 (\log \mathcal R_v)' \le-1+\frac{3(1.38)}{1+e^{1.38b}}<0
 \quad(b\ge.99).
\]
The last strict inequality is certified by exp(1.3662)>3.14.
For v=.6, dropping the denominator produces a decreasing upper function,
because kappa=.18>0 and each remaining factor decreases.
The exact scalar checks consequently show
\[
 R<q_0=.6\quad(b\ge.99),\qquad
 R<q_1=.2\quad(b\ge3).
\]
For the second bound drop the denominator for both endpoints and evaluate
the decreasing upper functions at b=3.
These ratio bounds are continuous-domain implications, not a sampled beta
grid. At the initial node beta=beta0. At each in-region pre-node with
beta>=beta0, F=F_E(1-R)>0, so the next beta increases and projection is
inactive. This simultaneous induction supplies beta positivity, rather
than assuming it to justify the force bound. Also 0<Delta beta<=d_max.
In particular the would-be post-node satisfies beta_n<=B+d_max.

## S.8.2 Exact real-radius budget

For u>=0, calculus gives
u K(u)<=4u exp(-2u)<=2/e<3/4 and
u K(-u)<=4u exp(-u)<=4/e<3/2.
The exact series for e proves e>8/3.
Therefore, in the stopped region, using ||grad d||<=2/r,
\[
 ||G_e||\le\frac{2(.951)(3/4)}{(.95)(.19)}<8,\quad
 ||G_h||\le\frac{2(.051)(3/2)}{(.95)(1.38)}<.12.
\]
The exact radial identity Delta s_i=alpha^2||G_i||^2 now proves, even at
the first exiting post-node,
\[
 s_-\le s_{e,k}\le S_e=1.05^2+N\alpha^2 8^2=1.1537,\quad
 s_-\le s_{h,k}\le S_h=1.05^2+N\alpha^2(.12)^2.
\]
No fixed-radius approximation or GF invariant Q is used. A stronger Joint objective
descent lemma is unnecessary. These bounds use all N possible increments
but do not execute or interpolate them.

## S.8.3 Exact log-cos increment upper and lower bounds

Write L(phi)=-log cos phi on the positive Easy principal chart,
and u=x tan phi. At an in-region pre-node,
\[
 x\le\alpha\,2B(16/27)/s_-<.01,\qquad
 0<u\le\alpha(3/4)/s_-<1.
\]
The exact cosine map gives
\[
 \Delta L=-\log(1-u)+\tfrac12\log(1+x^2).
\]
Since x^2/u=alpha 4p_e beta cos^2(phi)K(beta g)/(s g)
<=alpha 3/(s_-g_-^2), rational comparisons yield
\[
 \Delta L\le\left[\frac1{1-u_{\max}}+
       \frac{3\alpha}{2s_-g_-^2}\right]u<1.002u.
\]
Moreover atan x>=x-x^3/3>=.999x. The increasing derivative tan(phi)
on the positive chart, including its post-node, yields
\[
 \Delta L\ge\tan\phi\,\Delta\phi\ge.999u.
\]
Because u=rho beta Delta beta/[s_e(1-R)], these become
\[
 \Delta L\le1.002\frac{\rho\beta\Delta\beta}{s_-(1-R)},\qquad
 \Delta L\ge.999\frac{\rho\beta\Delta\beta}{S_e}.
\]
Both inequalities are for the actual atan update and changing radii.
The upper inequality needs only pre-node bounds; X_+>0 makes its post-node
logarithm defined even at a hypothetical exit.

## S.8.4 The beta-three prefix, crossing step, and angle exits

For any prefix with in-region pre-nodes, beta increases and
\[
 \sum_{k<n}\beta_k\Delta\beta_k
 =\tfrac12[\beta_n^2-\beta_0^2-\sum_{k<n}(\Delta\beta_k)^2]
 \le\beta_n^2/2.
\]
The indices whose pre-beta is below 3 form one prefix. Its final post-beta,
including the possible crossing of 3, is at most 3+d_max; thus the same
sum on those indices is at most (3+d_max)^2/2.
Define I0=(B+d_max)^2/2 and I3=(3+d_max)^2/2. The two ratio bounds give
\[
 I_E=\frac{I_0}{1-q_1}
       +\left(\frac1{1-q_0}-\frac1{1-q_1}\right)I_3,\quad
 I_H=\frac{q_1 I_0}{1-q_1}
       +\left(\frac{q_0}{1-q_0}-\frac{q_1}{1-q_1}\right)I_3.
\]
Consequently L(phi_e,n)-L(phi_e0)<=U_E=1.002 rho I_E/s_-.
Using cos^2 phi_e0=1-g0^2/4>=1-.21^2/4, the exact check
\[
 \exp(2U_E)<\frac{1-.21^2/4}{1-.6^2/4}
\]
implies g_n<.6. This excludes an Easy exit, including the full post-step.

For Hard, atan x<=x and cos<=1 imply
Delta phi_h<=2rho beta Delta beta R/[s_- a_-(1-R)].
Summing the same two prefixes gives
\[
 \phi_{h,n}-\phi_{h0}\le U_H=2\rho I_H/(s_-a_-)<.02.
\]
The rational U_H is approximately .0092723455766. This is a continuous-box
bound on the entire discrete prefix, not an observed path displacement.

## S.8.5 The beta-eighteen implication and first-crossing barrier

The lower Easy step inequality and Delta beta<=d_max give, at any in-region
node with beta_k>=18,
\[
 2[L(\phi_{e,k})-L(\phi_{e0})]\ge
 \frac{.999\rho}{S_e}
 [\beta_k^2-\beta_+^2-d_{\max}(\beta_k-\beta_-)]
 \ge T_{18},
\]
where beta_+=1.01, beta_-=.99 and
T18=.999 rho[18^2-1.01^2-d_max(18-.99)]/S_e.
The polynomial is increasing for beta>=18. Exact initial identities give
cos^2 phi_e0<=1-.19^2/4. An exponential enclosure proves
\[
 (1-.19^2/4)e^{-T_{18}}<1-(3/8)^2/4.
\]
Thus g_k>3/8 whenever pre-beta>=18. For beta>=18 and g>=3/8,
g exp(-2beta g) decreases in both beta and g. Therefore
\[
 0<F_k\le F_E\le4g e^{-2\beta g}
 \le F_{18}=\tfrac32e^{-27/2}.
\]
If beta has never reached 18 by n, it cannot exit 20.
Otherwise let m be its first crossing of 18. The crossing step has
beta_m<=18+d_max. All subsequent pre-nodes before n have beta>=18 and
satisfy the lower-gap implication just proved. Since (n-m)eta<=Neta=400000,
\[
 \beta_n\le18+d_{\max}+400000F_{18}<20.
\]
The rigorous scalar upper bound is approximately 19.05961249.
This includes both the threshold-crossing overshoot and the final would-be
exiting step; there is no estimate at a fictitious continuous terminal time.

Together S.8.4 and S.8.5 exclude every upper barrier at the first exit.
Global chart monotonicity already supplies all lower barriers.
Thus the region is invariant through all nodes 0..N, beta increases and
projection is inactive. Hard phi_h<=-.79+.02=-.77 gives
h<=-2sin(.77)<-1.38<0 uniformly.


Every argument used only in-region pre-nodes, while bounding the candidate exiting post-node without assuming it was already in-region. Radius increments use at most $N$ transitions. The beta-three prefix includes its crossing post-step and the beta-eighteen argument includes its first-crossing overshoot and the last candidate step. Global chart monotonicity supplies all lower barriers. Thus by first-exit induction all nodes $0,\ldots,N$ and pre-steps $0,\ldots,N-1$ are covered, uniformly by closed-box extrema. There are no omitted endpoints, unresolved subboxes or interpolated time intervals. In particular $g_0\le g_{J,k}<.6$, $\beta_0\le\beta_{J,k}<20$ and $h_{J,k}<-1.38$ at every integer node.

# S.9 GD Hold descent, integer hits, persistence, and risk

This argument applies separately for every $\xi\in K_0$, every $0<\rho\le.001$, and every $0<\eta\le.2$; it does not depend on the Joint cutoff. Beta is fixed at the instance's $\beta_0$. Let $G_i=\nabla_{w_i}J$ and let $G$ be the combined column gradient. Along the tangent update segment $w_i-\tau\alpha G_i$, $0\le\tau\le1$, orthogonality at the starting node yields
\[
 \|w_i-\tau\alpha G_i\|^2=s_i+\tau^2\alpha^2\|G_i\|^2\ge s_i\ge r_-^2 .
\]
Direct differentiation gives
\[
 \nabla d=2e_Y/r-2Yw/r^3,\qquad
 \nabla^2d=-2(e_Yw^\top+we_Y^\top+YI)/r^3+6Yww^\top/r^5 .
\]
Consequently $\|\nabla d\|\le2/r$ and $\|\nabla^2d\|\le12/r^2$. Combining these with the kernel derivative bounds, the fixed-beta Hessian on every such segment is at most
\[
 L_H=\frac{128\beta_+^2+192\beta_+}{27s_-}<16 .
\]
Each group multiplies a separate column block by $p_i\le1$, with no off-diagonal column block. For $\alpha\le1/5000$, $\alpha L_H<1$. Taylor's integral remainder along the actual segment proves
\[
 J_k-J_{k+1}\ge(\alpha-\alpha^2L_H/2)\|G_k\|^2
 \ge(\alpha/2)\|G_k\|^2 .
\]
Since $0\le J$ and $J_0\le2$, summing the exact radial identity gives
\[
 \sum_i(s_{i,n}-s_{i,0})=\alpha^2\sum_{k<n}\|G_k\|^2
 \le2\alpha J_0\le4\alpha .
\]
Thus every radius satisfies $s_{i,k}\le S=1.05^2+4/5000$. The Hessian bound was obtained before using this upper radius budget; there is no circular descent argument.

The exact map satisfies $0<x_i\le\alpha32\beta_+/(27s_-)<.01$. Integration of $(1+t^2)^{-1}$ gives
$\arctan x\ge x-x^3/3\ge.999x$ on this range. Until the hard gap reaches $.2$, its angle length is less than $.911$, its cosine exceeds $.68$, and its kernel exceeds $.4$ on the same interval $[-1.4645,.202]$ as in S.5. Each pre-hit step therefore advances its angle by at least $\alpha v_H$, where
\[
 v_H=.999\cdot2(.049)(.99)(.68)(.4)/S .
\]
A hit must have occurred by $m_H=\lceil.911/(\alpha v_H)\rceil$: if not, the sum of $m_H$ lower increments would exceed the initial remaining distance. Its integer bound includes the final overshoot:
\[
 \alpha m_H<.911/v_H+\alpha\le.911/v_H+1/5000<40 .
\]
For the easy group, the event is at zero if $g_0\ge.2$; otherwise its extra angle length is below $.006$, cosine exceeds $.99$, and
\[
 v_E=.999\cdot2(.949)(.99)^2(.4)/S,\qquad
 \alpha m_E<.006/v_E+1/5000<40 .
\]
For the exact $N=\lceil40/\alpha\rceil$, $\alpha N\ge40$, so both hits occur by $N$. The positive first-coordinate factor and the exact positive atan increments keep both gaps increasing on the principal chart at all later finite nodes. This proves persistence, including after an overshooting hit, directly for GD.

At $N$, the S.7 regime or the single S.8 anchor supplies $h_J<0$, and this section supplies both Hold gaps at least $\gamma$. Apply the exact risk derivation of S.5, now to the learned GD directions:
\[
 \inf_{b\ge0}R_M^J(N;b,\xi)\ge p_\xi M/(M+1),\qquad
 R_M^H(N;b_M^K,\xi)\le49/4000,\qquad
 \inf_{b\ge0}R_M^J-R_M^H(N;b_M^K,\xi)\ge49/4000 .
\]
This holds for every finite integer $M\ge1$. The same bound holds with both arms at the common scale. All actual budgets are retained, with $N\eta\in[40/\rho,40/\rho+\eta)$. Equal counts are not equal FLOPs or wall time.

The two GD scopes are distinct: S.7 certifies all $0<\rho\le10^{-9}$ and all $0<\eta\le.2$ over $K_0$; S.8 certifies exactly $(10^{-4},.2)$ over the entire closed box. C0/C7/C8 at the anchor are corollaries. Neither intervening rho values nor every smaller eta at the anchor follows.

# S.10 Exact scalar enclosures, checker contract, and provenance

For a nonnegative rational $x$, the positive exponential series through degree $n$ satisfies
\[
 S_n(x)=\sum_{j=0}^n x^j/j!\le e^x
 \le S_n(x)+\frac{x^{n+1}/(n+1)!}{1-x/(n+2)}
 \quad(0\le x<n+2).
\]
The first omitted term is explicit and each subsequent term ratio is at most $x/(n+2)<1$, proving the geometric tail. For negative inputs, reverse reciprocal endpoints. For sine/cosine, consecutive alternating partial sums enclose the value whenever term magnitudes decrease to zero; the error has the next term's sign and at most its magnitude. All used inputs and remainder domains are rational and all basic operations are exact Fraction arithmetic. The exp/log inverse implication $\log10<7/3$ uses the degree-nine positive partial sum at $7/3$. No rounded logarithm, asin or library call is promoted to a scalar enclosure.

STEP07's trigonometric and Hold interval endpoints follow from these enclosing operations. The square-root and logarithmic comparisons for $b_\xi$ are proved algebraically and by integrating $1/t$, rather than evaluating an unrounded transcendental initialization on a computer. The continuous force-ratio domain reductions in S.3 and S.8 remain analytic lemmas; they are not replaced by finite grids.

STEP09 generation uses degree48 exponential and twelve-term alternating trigonometric enclosures. The separately implemented checker uses degree64 and fourteen terms. It reconstructs exact rational expressions and tighter enclosing expressions without importing the generator. For supplied scalar enclosures it requires the independent enclosure to lie within the supplied one; for rational formulas it requires equality; for sufficient transcendental upper bounds it requires the supplied bound to contain the independently reconstructed upper and to meet the strict threshold. A computed high-precision point is not used in these implications.

The V2 finite-witness contract requires all nine bound keys. Eight must equal independently reconstructed rational expressions. The beta-after-first18 bound must equal its scalar certificate upper, contain the independent exponential upper, and be strictly below 20. It also checks the exact registered K0 and anchor, simultaneous pre-state order, gradient factor and no loss half-factor, actual radius and atan identities, the complete node/step block, initial node, final post-node and beta-split overshoot. Eleven semantic fixtures invalidate the gradient factor, update order, radius map, angle map, domain endpoint, ceil count, final block node, growth factor, beta upper, unknown key and missing key. A semantic failure reason, not a thrown exception, counts as detection.

The preserved V1 checker lacked the complete bound-key and beta witness checks; this was a checker coverage defect, not a mathematical counterexample or a correction to the actual scalar witness. STEP09 V2 closed that defect, preserving V1 and its review history. The checker verifies arithmetic and the explicit witness contract. The English proofs above establish the logical inductions and uniform quantifiers; neither the checker nor an agent opinion is a formal proof assistant.

The source inventory and crosswalk identify every used source by path, SHA256 and locator. STEP06's base point and $1/80$ rule, STEP07's whole-box GF laws, STEP08's original strict cutoff and numerical runs, and STEP09's closed addendum and anchor are preserved separately. Notation changes, including $\nu$ for the GF upper buffer and $\zeta$ for Hold slow time, are registered without changing constants or quantifiers.

The 27 prescribed GF paths and nine initialization points are finite diagnostics, not a box supremum. STEP08's 36 original main paths execute 51,600,006 updates, with 57,335,772 recorded including auxiliaries. STEP09 runs zero new trajectories and reuses six anchor paths, representing 12 million parent updates. Seventy-two STEP08 raw comparisons include 54 favoring Joint; their common-scale contrasts have a different meaning. The Matrix Bridge is a separate finite-query, learnable-QK experiment: later ranking and larger accumulated hard risk coexist with lower final raw risk under Joint. It is not a transfer theorem. Original E05/D5 shortfalls, original_full_G0_passed=false and old DSR confirmations NOT_RUN are unchanged.

No result here proves arbitrary-query, free-QK, learned-readout or finite-sample generalization, SGD/Adam behavior, GD exponential sharp escape, a maximal cutoff, intermediate rho coverage, a GF time prefactor, or whole-path float64 rounding. The leading coefficient's absence of $p,\beta_0,r_h$ is not independence of the full time or its unproved prefactor. The supplement is a proof/reproducibility deliverable, not a new scientific experiment.
