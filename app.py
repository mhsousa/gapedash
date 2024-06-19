import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.image("gape.png")

tab1, tab2, tab3, tab4 = st.tabs(["Inflação","Emprego", "Renda", "Desigualdade"])
tab1.subheader("Inflação - 2020 a 2024")
tab2.subheader("Emprego - 2001 a 2018")
tab3.subheader("Renda - 2012 a 2023")
tab4.subheader("Desigualdade - 2012 a 2023")
df_emp = pd.read_excel("giniMA2012_2023.xlsx", sheet_name="Criacao_Empreg._Formais_MA")
df_inf = pd.read_excel("giniMA2012_2023.xlsx", sheet_name="Inflação_Mensal_Slz")

with tab1:
    #Inicio gráfico 1
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Inflação Mensal SLZ (%)"],
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line_color='rgba(255,255,255,0)',
        showlegend=False,
        name='Inflação Mensal SLZ (%)',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Habitação"],
        fill='toself',
        fillcolor='rgba(255,255,0)',
        line_color='rgba(255,255,0)',
        name='Habitação',
        showlegend=False,
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Artigos de residência"],
        fill='toself',
        fillcolor='rgba(124,252,0)',
        line_color='rgba(124,252,0)',
        showlegend=False,
        name='Artigos de residência',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Vestuário"],
        fill='toself',
        fillcolor='rgba(0,255,255)',
        line_color='rgba(0,255,255)',
        showlegend=False,
        name='Vestuário',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Transportes"],
        fill='toself',
        fillcolor='rgba(138,43,226)',
        line_color='rgba(138,43,226)',
        name='Transportes',
        showlegend=False,
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Saúde e cuidados pessoais"],
        fill='toself',
        fillcolor='rgba(255,0,0)',
        line_color='rgba(255,0,0)',
        showlegend=False,
        name='Saúde e cuidados pessoais',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Despesas pessoais"],
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line_color='rgba(255,255,255,0)',
        showlegend=False,
        name='Despesas pessoais',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Educação"],
        fill='toself',
        fillcolor='rgba(0,176,246,0.2)',
        line_color='rgba(255,255,255,0)',
        name='Educação',
        showlegend=False,
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"],
        y=df_inf["Comunicação"],
        fill='toself',
        fillcolor='rgba(231,107,243,0.2)',
        line_color='rgba(255,255,255,0)',
        showlegend=False,
        name='Comunicação',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Inflação Mensal SLZ (%)"],
        line_color='rgb(0,100,80)',
        name='Inflação Mensal SLZ (%)',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Habitação"],
        line_color='rgb(255,255,0)',
        name='Habitação',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Artigos de residência"],
        line_color='rgb(124,252,0)',
        name='Artigos de residência',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Vestuário"],
        line_color='rgb(0,255,255)',
        name='Vestuário',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Transportes"],
        line_color='rgb(138,43,226)',
        name='Transportes',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Saúde e cuidados pessoais"],
        line_color='rgb(255,0,0)',
        name='Saúde e cuidados pessoais',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Despesas pessoais"],
        line_color='rgb(0,100,80)',
        name='Despesas pessoais',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Educação"],
        line_color='rgb(0,176,246)',
        name='Educação',
    ))
    fig.add_trace(go.Scatter(
        x=df_inf["Mês"], y=df_inf["Comunicação"],
        line_color='rgb(231,107,243)',
        name='Comunicação',
    ))
    fig.update_traces(mode='lines')
    fig.update_layout(title="Inflação Mensal em São Luís - MA")
    
    #Final Gráfico 1
    st.plotly_chart(fig)
    st.write("Comentários sobre o gráfico 1")

with tab2:
    fig = px.line(df_emp, x='Ano', y="Taxa de Criação de Empregos - %")
    fig.update_layout(
        title="Taxa de Criação de Empregos")


    fig2 = px.line(df_emp, x='Ano', y="Taxa de Destruição de Empregos - %")
    fig2.update_layout(
            title="Taxa de Destruição de Empregos"
      
        )

    fig3 = px.line(df_emp, x='Ano', y="Taxa de Variação Líquida de Empregos - %")
    fig3.update_layout(
            title="Taxa de Variação Liquida de Empregos"
        )


    st.plotly_chart(fig)
    st.write("Comentários sobre o gráfico 1")
    st.plotly_chart(fig2)
    st.write("Comentários sobre o gráfico 2")
    st.plotly_chart(fig3)
    st.write("Comentários sobre o gráfico 3")
        

with tab3:
    st.write("Renda")


with tab4:
    st.write("Desigualdade")
