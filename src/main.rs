use crate::Graph::G;
mod Test;
mod Graph;

fn main() {
    //dbg!(Graph::gen(10));
    //Test::graphic(200);
    let graph_test:Graph::G = Graph::gen(10);
    dbg!(Graph::join(graph_test, 4, 6));
}
