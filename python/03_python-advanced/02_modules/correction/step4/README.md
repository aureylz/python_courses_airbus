# Answers to questions #
The main difference is that python interpreter behave differently when you load a file from interpreter:
```bash
python main.py
```
compared to loading a file from an ```import``` statement

```python
import greeting
```

This is why the following code
```python
if __name__ == "__main__":
```
is executed only from the ```main.py``` file.