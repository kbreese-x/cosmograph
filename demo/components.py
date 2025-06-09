import gradio as gr


LIST_OF_STATES = [
    "AL",
    "AK",
    "AZ",
    "AR",
    "CA",
    "CO",
    "CT",
    "DE",
    "FL",
    "GA",
    "HI",
    "ID",
    "IL",
    "IN",
    "IA",
    "KS",
    "KY",
    "LA",
    "ME",
    "MD",
    "MA",
    "MI",
    "MN",
    "MS",
    "MO",
    "MT",
    "NE",
    "NV",
    "NH",
    "NJ",
    "NM",
    "NY",
    "NC",
    "ND",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VT",
    "VA",
    "WA",
    "WV",
    "WI",
    "WY",
]

def create_title(title: str | list[str], subtitle: str = "", **kwargs) -> gr.HTML:
    title_html = ""
    html_tag = "<div class='stylized-text' {inline_style}>{text}</div>"

    title = [title] if not isinstance(title, list) else title

    for text in title:
        title_html += html_tag.format(text=text, inline_style="") + "\n"

    subtitle_html = (
        html_tag.format(text=subtitle, inline_style='style="font-size: 26px"')
        if subtitle
        else ""
    )

    title_component = gr.HTML(
        f"""
                <div class="title-container">
                    {title_html}
                    {subtitle_html}
                </div>
                
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@800&display=swap');
                .title-container {{
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                }}
                .stylized-text {{
                    font-family: 'Urbanist', sans-serif;
                    font-weight: 800;
                    font-size: 32px;
                    letter-spacing: -1px;
                    text-transform: uppercase;
                    background: radial-gradient(#4cc3ff, #0077be);
                    background-size: 100%;
                    background-clip: text;
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    text-align: center;
                }}
                </style>
                """,
        **kwargs,
    )
    return title_component

# __all__ = [
#     "LIST_OF_STATES",
#     "create_title",
# ]

if __name__ == "__main__":
    title = create_title(
        ["XIFIN Agents", "Demo Application"],
        "A Gradio demo application for XIFIN Agents",
    )
    print(title.value)

