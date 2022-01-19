class School {
  type DB = Map[Int, Seq[String]]
  def add(name: String, g: Int) = {
      db(g) = grade(g)+: name
      // how do i acces db
  }
  def db: DB = Map.empty
  def grade(g: Int): Seq[String] = db.getOrElse(g,Nil)
  def sorted: DB = ???
}

