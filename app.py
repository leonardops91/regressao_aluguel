# %%
import gradio as gr
import pandas as pd
import joblib

# %%
model = joblib.load('./modelo_aluguel.pkl')

# %%
def predict(tamanho_m2, n_quartos, idade_casa, garagem, localizacao):
    
    dados = {
    'tamanho_m2': tamanho_m2, 
    'n_quartos': n_quartos, 
    'idade_casa': idade_casa, 
    'garagem': garagem,
    'localizacao_periferia': localizacao == 'Periferia', 
    'localizacao_suburbio': localizacao == 'Subúrbio'
    }
    sample = pd.DataFrame(dados, index=[1])
    aluguel = model.predict(sample)
    aluguel_number = round(float(aluguel[0]), 2)
    return aluguel_number

# %%
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Slider(30, 300, step=1),
        gr.Number(minimum=1, maximum=10),
        gr.Slider(0, 50, step=1),
        gr.Number(minimum=0, maximum=10),
        gr.Radio(['Periferia', 'Subúrbio'])
    ],
    outputs=['number']
)

# %%
demo.launch()

# %%



