<div align="center">

# CartPole RL Methods

**Tabular Q-learning, REINFORCE, and model-based LQR on CartPole-v1 with live visualization.**

[Methods](#method-map) | [Run](#run) | [Files](#project-layout)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Gymnasium](https://img.shields.io/badge/Gymnasium-CartPole--v1-0B7285?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-web_dashboard-009688?style=flat-square)
![Pygame](https://img.shields.io/badge/Pygame-desktop_visualizer-495057?style=flat-square)

</div>

---

## Focus

This repository compares simple reinforcement-learning and control approaches on the classic CartPole balancing task.

The flow is direct:

1. Start with tabular Q-learning and state discretization.
2. Move to policy-gradient learning with REINFORCE.
3. Contrast both learned methods with a model-based LQR controller.
4. Visualize behavior through a desktop Pygame renderer or a browser dashboard.

## Method Map

| Method | File | Purpose |
| --- | --- | --- |
| Q-learning | [`q_agent.py`](q_agent.py), [`q_learning.py`](q_learning.py) | Value-based baseline using a discretized state space. |
| Policy gradient | [`policy_gradient.py`](policy_gradient.py), [`policy_gradient_simple.py`](policy_gradient_simple.py) | REINFORCE agents using PyTorch or a small NumPy network. |
| Model-based LQR | [`model_based.py`](model_based.py) | Analytical controller used as a model-based comparison point. |
| Desktop visualization | [`train_pygame.py`](train_pygame.py) | Live Pygame animation for Q-learning. |
| Web visualization | [`train_web.py`](train_web.py) | FastAPI and WebSocket dashboard for Q-learning, policy gradient, and LQR. |
| Launcher | [`run_animation.py`](run_animation.py) | Convenience entry point for desktop or web demos. |

## Run

Create an environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the desktop visualizer:

```powershell
python run_animation.py pygame --episodes 500
```

Run the web dashboard:

```powershell
python run_animation.py web
```

Then open:

```text
http://127.0.0.1:8000
```

You can also run the server directly:

```powershell
uvicorn train_web:app --reload --host 127.0.0.1 --port 8000
```

## Project Layout

```text
.
  q_agent.py
  q_learning.py
  policy_gradient.py
  policy_gradient_simple.py
  model_based.py
  train_pygame.py
  train_web.py
  run_animation.py
  requirements.txt
```

## Notes

- CartPole has continuous observations, so the tabular Q-learning agent discretizes the state.
- The policy-gradient agents use raw continuous states.
- LQR does not learn from episodes; it uses an analytical controller from a linearized model.
- Generated caches, virtual environments, logs, and model artifacts are excluded from Git.
