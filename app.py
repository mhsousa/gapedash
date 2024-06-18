import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Dashboard - GAPE")



df = pd.read_excel("giniMA2012_2023.xlsx", sheet_name="Criacao_Empreg._Formais_MA")
fig = px.line(df, x='Ano', y="Taxa de Criação de Empregos - %")
fig.update_layout(
        xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="<br><sup>Taxa de Criação de Empregos - %</sup>",
            font=dict(size=25)
            )
        )
    )


fig2 = px.line(df, x='Ano', y="Taxa de Destruição de Empregos - %")
fig2.update_layout(
        xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="<br><sup>Taxa de Destruição de Empregos - %</sup>",
            font=dict(size=25)
            )
        )
    )

fig3 = px.line(df, x='Ano', y="Taxa de Variação Líquida de Empregos - %")
fig3.update_layout(
        xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text="<br><sup>Taxa de Variação Líquida de Empregos - %</sup>",
            font=dict(size=25)
            )
        )
    )


st.plotly_chart(fig)
st.text("Comentários sobre o gráfico 1")
st.plotly_chart(fig2)
st.text("Comentários sobre o gráfico 2")
st.plotly_chart(fig3)
st.text("Comentários sobre o gráfico 3")
    

