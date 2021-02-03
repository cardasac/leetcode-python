FILES=(solutions tests)

black "${FILES[@]}" --line-length 79
pylint "${FILES[@]}"
flake8 "${FILES[@]}"
