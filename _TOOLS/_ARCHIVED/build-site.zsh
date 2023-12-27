echo "*** Building Site"

# Publish folder
# PUBLISH_FOLDER = _PUBLISHED
# CONTENT_FOLDER = _Content
# PARTIALS_FOLDER = _Partials

# Build Navigation
echo "*** Building Navigation..."
pandoc _Partials/_navigation.md -t html --output _PUBLISHED/_navigation.html


echo "*** Converting Markdown files to HTML"

# HTML
pandoc _Content/index.md -t html --standalone --css=../_Styles/main.css -A _PUBLISHED/_navigation.html --output _PUBLISHED/index.html
pandoc _Content/jro-tech-stack.md -t html --standalone  --css=../_Styles/main.css -A _PUBLISHED/_navigation.html --output _PUBLISHED/jro-tech-stack.html
pandoc _Content/contact-jro.md -t html --standalone  --css=../_Styles/main.css -A _PUBLISHED/_navigation.html --output _PUBLISHED/contact-jro.html
pandoc _Content/about-website.md -t html --standalone  --css=../_Styles/main.css -A _PUBLISHED/_navigation.html --output _PUBLISHED/about-website.html
pandoc _Content/priority-goals.md -t html --standalone  --css=../_Styles/main.css -A _PUBLISHED/_navigation.html --output _PUBLISHED/priority-goals.html
pandoc _Content/25-million-usd.md -t html --standalone  --css=../_Styles/main.css -A _PUBLISHED/_navigation.html --output _PUBLISHED/25-million-usd.html
pandoc _Content/TCS-priority-goals.md -t html --standalone  --css=https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css  --output _PUBLISHED/TCS-priority-outcomes.html

# PDF
pandoc _Content/priority-goals.md -t pdf --output _PUBLISHED/priority-goals.pdf

#for filename in _Content/*.md;
#do
#    # Get local Filename without, without extention of directory
#    echo "Working on file: $filename"
#    echo pandoc $filename -t html --standalone -A _PUBLISHED/_navigation.html --output _PUBLISHED/$filename.html
#done

echo "*** Site Build Completed"


# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
