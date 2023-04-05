from dash import html, dcc, dash_table
import pandas as pd

def draw_table(data={}):
  table = data["table"]
  total = data["total"]

  df = pd.DataFrame(table)
  return [html.Label(f"Found {total} molecules"),
          dash_table.DataTable(df.to_dict('records'), 
                              [{"name": i, "id": i} for i in df.columns],
                              )]