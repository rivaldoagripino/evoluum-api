param (
    [string]$action = "up"
)

if ($action -eq "up-build") {
    docker-compose up --build
}
elseif ($action -eq "up") {
    docker-compose up
}
elseif ($action -eq "down") {
    docker-compose down
}
elseif ($action -eq "shell") {
    docker-compose exec app /bin/sh
}
elseif ($action -eq "migrate") {
    docker-compose exec app alembic upgrade head
}
elseif ($action -eq "test") {
    docker-compose exec app pytest
}
elseif ($action -eq "code-convention") {
    flake8
    pycodestyle
}
