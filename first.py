import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    a = 45
    return (a,)


@app.cell
def _():
    b = 56
    return (b,)


@app.cell
def _(mo):
    c = mo.ui.slider(1, 100, 1)
    return (c,)


@app.cell
def _(c):
    c
    return


@app.cell
def _(a, b, c, mo):
    mo.md(f"""
     A = 45
     B = 56
     C = {c.value}
 
     $A + B + C =$ {a+b+c.value}
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
