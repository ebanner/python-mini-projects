# python-time

Convert from seconds to minutes and minutes to seconds

## Files

- [time.py](https://github.com/ebanner/python-time/blob/main/main.py)
- [Time.ipynb](https://github.com/ebanner/python-time/blob/main/Time.ipynb)

## Demo

### Minutes → Seconds

$$
x \ \text{min} * \frac{60 \text{sec}}{1 \text{min}} \rightarrow 60x \ \text{sec}
$$


```python
minutes = 60

seconds = minutes * 60
seconds # → 3600
```

### Seconds → Minutes

$$
x \ \text{sec} * \frac{1 \text{min}}{60 \text{sec}} \rightarrow \frac{x}{60} \ \text{min}
$$


```python
seconds = 3600

minutes = seconds // 60
minutes # → 60
```
