## Import neccessary libraries
from functools import lru_cache
from pathlib import Path

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import joblib

from dash import Dash, html
from dash.dependencies import Input, Output

# Import the model
BASE_PATH = Path.cwd().parent.parent
MODEL_PATH = BASE_PATH / "models"


@lru_cache
def get_model():
    return joblib.load(MODEL_PATH / "best_rf_stroke_merged.model")


external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1(
                            "Stroke Risk Calculator",
                            style={"color": "#347571", "fontSize": "70px"},
                        ),
                        html.H5(
                            "Welcome to Team Tria-nauts' Stroke Risk Calculator! Predict your risk of developing stroke disease based on the likelihood someone similar to you has had a stroke using our Machine Learning model trained using approximately 430,000 survey responses from U.S. Residents collected by The CDC BRFSS."
                        ),
                        html.H5(
                            "This calculator utilizes carefully picked out parameters ranging from factors such as BMI to smoking status, and aims to produce a binary response as to whether an individual is at risk for a stroke, with an accuracy of approximately 93%."
                        ),
                        html.H5(
                            "DISCLAIMER: The following calculator was produced as a part of RBC Borealis AI's Let's SOLVE It Program, by a team of three first-year computer science students from the University of Waterloo."
                        ),
                        html.H5(
                            "This is NOT a substitute for a medically-accurate stroke risk calculator. Please reach out to your family doctor/nearest health facility if you believe to be at risk of a stroke/need immediate medical attention."
                        ),
                        html.H5(
                            "Alternatively, feel free to check out the following stroke risk calculators:"
                        ),
                        html.A(
                            "https://clincalc.com/Cardiology/ASCVD/PooledCohort.aspx",
                            href="https://clincalc.com/Cardiology/ASCVD/PooledCohort.aspx",
                            target="blank",
                            style={"font-size": "18px"},
                        ),
                        html.Br(),
                        html.A(
                            "https://www.projectbiglife.ca/cardiovascular-disease",
                            href="https://www.projectbiglife.ca/cardiovascular-disease",
                            target="blank",
                            style={"font-size": "18px"},
                        ),
                    ],
                    width=20,
                )
            ],
            justify="center",
            align="center",
        ),
        html.Br(),
        dbc.Row(
            [
                # Health Care Access CHECKUP1
                dbc.Col(
                    [
                        html.H6(
                            "About how long has it been since you last visited a doctor for a routine checkup?",
                            style={
                                "align-items": "center",
                                "justify-content": "center",
                            },
                        ),
                    ],
                    width=6,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Within past year",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Within past 2 years",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Within past 5 years",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 3,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Five or more years ago",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 4,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Refuse to Answer",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="health-care-access",
                            placeholder="Healthcare Access...",
                            style={
                                "margin-top": "25px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
                # High Cholesterol
                # TOLDHI3
                dbc.Col(
                    [
                        html.H6(
                            "Have you ever been told by a doctor, nurse, or other health professional that your cholesterol is high?"
                        ),
                    ],
                    width=6,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Refuse to Answer",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="cholesterol-high",
                            placeholder="Cholesterol...",
                            style={
                                "margin-top": "30px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                # Smoke cigarettes Regularly LCSFIRST
                dbc.Col(
                    [
                        html.H6("Have you ever smoked a cigarette?"),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 0,
                                },
                            ],
                            id="lcsfirst",
                            placeholder="Ever Smoked Status...",
                            style={
                                "margin-top": "12px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
                # Cancer CNCRTYP1
                dbc.Col(
                    [
                        html.H6("(Ever told) (you had) cancer?"),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                            ],
                            id="cancer-status",
                            placeholder="Cancer Status...",
                            style={
                                "margin-top": "12px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                # Kidney Disease CHCKDNY2
                dbc.Col(
                    [
                        html.H6(
                            "Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?"
                        ),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Refuse to Answer",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="kidney-disease",
                            placeholder="Kidney Disease Status...",
                            style={
                                "margin-top": "26px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
                # Good
                #  Diabetes DIABETE4
                # Actually Good
                dbc.Col(
                    [
                        html.H6("(Ever told) (you had) diabetes?"),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes, but female told during pregnancy",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 3,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No, pre-diabetes or borderline diabetes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 4,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Refuse to Answer",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="diabetes",
                            placeholder="Diabetes Status...",
                            style={
                                "margin-top": "25px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                # Ecigarette ECIGNOW1
                dbc.Col(
                    [
                        html.H6(
                            "Do you now use e-cigarettes or other electronic vaping products every day, some days, or not at all?"
                        ),
                    ],
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Every Day",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Some days",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Not at all",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 3,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Never used e-cigs",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 4,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Refuse to Answer",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="ecigarette",
                            placeholder="Ecigarette Usage Status...",
                            style={
                                "margin-top": "25px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
                # Alcohol ALCDAY5
                dbc.Col(
                    [
                        html.H6(
                            "During the past 30 days, have you consumed at least one alcoholic beverage?"
                        ),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 0,
                                },
                            ],
                            id="alcohol",
                            placeholder="Alcohol Usage Status...",
                            style={
                                "margin-top": "25px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                # Marijuana MARIJAN1
                dbc.Col(
                    [
                        html.H6(
                            "During the past 30 days, have you used marijuana or cannabis?"
                        ),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 0,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                            ],
                            id="cannabis",
                            placeholder="Cannabis Usage Status...",
                            style={
                                "margin-top": "20px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
                # Preferred Race _PRACE1
                dbc.Col(
                    [
                        html.H6("What race do you best identify as?"),
                    ],
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "20px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "White",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Black or African American",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "American Indian or Alaskan Native",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 3,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Asian",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 4,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Native Hawaiian or other Pacific Islander",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 5,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "None of the above/Do not know",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="race",
                            placeholder="Race...",
                            style={
                                "margin-top": "20px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                # Sex _SEX
                dbc.Col(
                    [
                        html.H6("What sex do you identify as?"),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Male",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Female",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "None of the Above",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="sex",
                            placeholder="Sex...",
                            style={
                                "margin-top": "15px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
                # Age _AGE_G
                dbc.Col(
                    [
                        html.H6("What age category do you belong in?"),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "18 to 44",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "25 to 34",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "35 to 44",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 3,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "45 to 54",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 4,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "55 to 64",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 5,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "65 or older",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 6,
                                },
                            ],
                            id="age",
                            placeholder="Age...",
                            style={
                                "margin-top": "13px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                # BMI _BMI5CAT
                dbc.Col(
                    [
                        html.H6("What Body Mass Index do you best identify as?"),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Underweight (BMI < 18.5)",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Normal Weight (18.5 <= BMI < 25.0)",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Overweight (25.0 <= BMI < 30.0)",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 3,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Obese (30.0 >= BMI)",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 4,
                                },
                            ],
                            id="bmi",
                            placeholder="BMI Status...",
                            style={
                                "margin-top": "15px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
                # Smoker _SMOKER3
                dbc.Col(
                    [
                        html.H6("What smoking status do you best identify as?"),
                    ],
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Current Smoker (smokes every day)",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Current Smoker (smokes some days)",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Former Smoker",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 3,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Never Smoked",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 4,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Do not know/Refuse to Answer",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="smoking-status",
                            placeholder="Smoking Status...",
                            style={
                                "margin-top": "15px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        html.Br(),
        dbc.Row(
            [
                # Heart Attack CVDINFR4
                dbc.Col(
                    [
                        html.H6(
                            "(Ever told) you had a heart attack, also called a myocardial infraction?"
                        ),
                    ],
                    align="center",
                    width=7,
                    lg=3,
                    className="border rounded border-success",
                    style={
                        "padding": "15px",
                        "background-color": "#198754",
                        "color": "white",
                    },
                ),
                dbc.Col(
                    [
                        dcc.Dropdown(
                            [
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Yes",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 1,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "No",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 2,
                                },
                                {
                                    "label": html.Span(
                                        [
                                            html.Span(
                                                "Refuse to Answer",
                                                style={
                                                    "font-size": 15,
                                                    "padding-left": 5,
                                                },
                                            ),
                                        ],
                                        style={
                                            "align-items": "center",
                                            "justify-content": "center",
                                        },
                                    ),
                                    "value": 9,
                                },
                            ],
                            id="heart-disease",
                            placeholder="Heart Attack Status...",
                            style={
                                "margin-top": "15px",
                                "width": "95%",
                                "textAlign": "left",
                                "align-items": "left",
                            },
                        )
                    ],
                    width=6,
                    lg=3,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col([]),
                dbc.Col(
                    [
                        dbc.Button(
                            children="Reset",
                            id="reset",
                            n_clicks=0,
                            size="lg",
                            color="success",
                            style={"margin-top": 90, "width": "200px"},
                        ),
                    ],
                    width=15,
                    lg=3,
                ),
                dbc.Col(
                    [
                        dbc.Button(
                            children="Calculate",
                            id="submit",
                            n_clicks=0,
                            size="lg",
                            color="success",
                            style={"margin-top": 90, "width": "200px"},
                        ),
                    ],
                    width=15,
                    lg=3,
                ),
                dbc.Col([]),
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                html.H3(
                    id="result",
                    children="Enter your information in the boxes above. Once all your information has been inputted, press Submit",
                    className="text-center",
                ),
            ]
        ),
        html.Br(),
        html.Br(),
    ]
)


@app.callback(
    Output("result", "children", allow_duplicate=True),
    [
        Input("submit", "n_clicks"),
        Input("reset", "n_clicks"),
        Input("health-care-access", "value"),
        Input("cholesterol-high", "value"),
        Input("heart-disease", "value"),
        Input("kidney-disease", "value"),
        Input("diabetes", "value"),
        Input("ecigarette", "value"),
        Input("alcohol", "value"),
        Input("lcsfirst", "value"),
        Input("cancer-status", "value"),
        Input("cannabis", "value"),
        Input("race", "value"),
        Input("sex", "value"),
        Input("age", "value"),
        Input("bmi", "value"),
        Input("smoking-status", "value"),
    ],
    prevent_initial_call=True,
)

# Order of input determines input order for the function
def calculator(
    submit_clicks,
    reset_clicks,
    health_care_access,
    cholesterol_high,
    heart_disease,
    kidney_disease,
    diabetes_value,
    ecigarette_value,
    alcohol_value,
    lcsfirst_value,
    cancer_status,
    cannabis_value,
    race_value,
    sex_value,
    age_value,
    bmi_value,
    smoking_status,
):
    output = None

    if (
        (health_care_access is not None)
        and (cholesterol_high is not None)
        and (heart_disease is not None)
        and (kidney_disease is not None)
        and (diabetes_value is not None)
        and (ecigarette_value is not None)
        and (alcohol_value is not None)
        and (race_value is not None)
        and (sex_value is not None)
        and (age_value is not None)
        and (bmi_value is not None)
        and (smoking_status is not None)
        and (cannabis_value is not None)
        and (cancer_status is not None)
        and (lcsfirst_value is not None)
    ):
        # Converting all values into floats
        health_care_access = float(health_care_access)
        cholesterol_high = float(cholesterol_high)
        heart_disease = float(heart_disease)
        kidney_disease = float(kidney_disease)
        diabetes_value = float(diabetes_value)
        ecigarette_value = float(ecigarette_value)
        alcohol_value = float(alcohol_value)
        race_value = float(race_value)
        sex_value = float(sex_value)
        age_value = float(age_value)
        bmi_value = float(bmi_value)
        smoking_status = float(smoking_status)
        cannabis_value = float(cannabis_value)
        cancer_status = float(cancer_status)
        lcsfirst_value = float(lcsfirst_value)

        output = get_model().predict(
            [
                [
                    health_care_access,
                    cholesterol_high,
                    heart_disease,
                    kidney_disease,
                    diabetes_value,
                    ecigarette_value,
                    alcohol_value,
                    race_value,
                    sex_value,
                    age_value,
                    bmi_value,
                    smoking_status,
                    cannabis_value,
                    cancer_status,
                    lcsfirst_value,
                ]
            ]
        )

    if submit_clicks > 0:
        if output == 1:
            return "Based on the information you entered, our model has found that yes, people with similar measures as yourself have been diagnosed with stroke in the past. You may be at risk for a stroke. Please press reset to make another prediction."
        elif output == 2:
            return "Based on the information you entered, our model has found that no, people with similar measures as yourself have not been diagnosed with stroke in the past. You are currently not at risk for a stroke. Please press reset to make another prediction."
        else:
            return (
                "Please fill out all the boxes above with correct input to get a result"
            )
    else:
        return "Enter your information in the boxes above. Once all your information has been inputted, press Calculate"


@app.callback(
    [
        Output("result", "children", allow_duplicate=True),
        Output("submit", "n_clicks"),
        Output("health-care-access", "value"),
        Output("cholesterol-high", "value"),
        Output("heart-disease", "value"),
        Output("kidney-disease", "value"),
        Output("diabetes", "value"),
        Output("ecigarette", "value"),
        Output("alcohol", "value"),
        Output("lcsfirst", "value"),
        Output("cancer-status", "value"),
        Output("cannabis", "value"),
        Output("race", "value"),
        Output("sex", "value"),
        Output("age", "value"),
        Output("bmi", "value"),
        Output("smoking-status", "value"),
    ],
    [Input("reset", "n_clicks")],
    prevent_initial_call=True,
)
def update(reset_clicks):
    return (
        "Enter your information in the boxes above. Once all your information has been inputted, press Calculate",
        0,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    )


if __name__ == "__main__":
    app.run_server()
