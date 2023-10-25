namespace py tutorial

struct Player {
    1: required string name,
    2: required string ip,
    3: required string email,
    4: i64 timestamp,
}

service ScoreboardService {
    Player registerPlayer(1: string name, 2: string email),
    list<Player> getScoreboard(),
}
