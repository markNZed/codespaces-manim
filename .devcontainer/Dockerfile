FROM manimcommunity/manim

USER root

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    xdg-utils \
    vlc \
    ffmpeg \
    git

# To avoid an error when running pip    
RUN mkdir /manim/.cache
# To avoid warning of empty plugins list in notebook
RUN pip install manim_plugintemplate
    
