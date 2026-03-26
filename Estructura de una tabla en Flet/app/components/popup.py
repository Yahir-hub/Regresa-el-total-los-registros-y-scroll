# app/components/popup.py
def show_popup(*args, **kwargs): pass
def show_popup_auto_close(*args, **kwargs): pass
async def show_snackbar(page, text, bgcolor="red"):
    print(f"SNACKBAR ERROR: {text}") # Imprime el error en consola si falla
def confirm_dialog(*args, **kwargs): pass