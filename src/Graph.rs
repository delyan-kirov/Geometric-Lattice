extern crate rand;
use rand::Rng;
use std::fmt;

pub struct G{
    pub E: Vec<Vec<u8>>,
    pub N: u8,
    pub P: Vec<u8>
}

//Creates a partition of n
fn set(n:usize) -> Vec<u8>{
    let mut out:Vec<u8> = vec![0];
    for i in 0..n{
        if i == 0{
            continue;
        }

        else if i == 1 { //initial value
            out.push(1);
        }

        else if i == n-1{ //final value
            out.push(out[i-1]+1)
        }

        else{ //at "random" the next point is decided
            if rand::thread_rng().gen_range(0, 12) > 4{
                out.push(out[i-1]+1);
            }
            else {
                out.push(out[i-1]);
            }
        }
    }
    return out;
}

impl Clone for G{
    fn clone(&self) -> G{
        let graph:G = G{E: (self.E.clone()), N: (self.N.clone()), P: (self.P.clone()) };
        return graph;
    }
}

impl fmt::Debug for G{
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("G")
         .field("E", &self.E)
         .field("N", &self.N)
         .field("P", &self.P)
         .finish()
    }
}

//finds the neighbour set of any vertex
fn neibors (graph:G, v:usize) -> Vec<usize>{
    let count:usize = graph.N as usize;
    let mut res:Vec<usize> = vec![];
    for i in 0..count{
        if graph.E[v][i] == 1{
            res.push(i);
        }
    }
    return res;
}

//breadth first search
pub fn bfs (graph:G) -> bool{
    //initialize start
    let len:usize = graph.E.len();
    let mut cycle:usize = 0;
    let mut discover:Vec<usize> = vec![0; len];
    discover[cycle] = 1;

    //start search
    while cycle <= len-1{
        let neibset = neibors(graph.clone(), cycle); //find neighbours
        let discover_reff:Vec<usize> = discover.clone(); //make a reference
        //add neighbours to discover
        for i in 0..len{
            if neibset.contains(&i) {
                discover[i] = 1;
            }
        }
        cycle = cycle + 1;
        //check if neighbours are already included
        let mut check:usize = 0;
        for i in 0..len {
            if discover[i] == discover_reff[i] {
                check = check.clone() + 1;
            }
        }
        if check == len {
            if discover.contains(&(0 as usize)) {
                return false;
            }
            else {
                return true;
            }
        }
    }
    if discover.contains(&(0 as usize)) {
        return false;
    }
    else {
        return true;
    }
}

pub fn gen (n:usize) -> G{

    let mut graph:G = G { E: (vec![vec![0]; n]), N: (n as u8), P: (vec![0, n as u8]) };
    let mut check:bool = false;

    while !check {
    let N:u8 = n as u8;
    let P:Vec<u8> = set(n);
    let mut E:Vec<Vec<u8>> = vec![vec![0]; n];
    for i in 0..n{
        for j in i..n{

            if i == 0{
                if j == 0{
                    continue;
                }
                else {
                    let keep:u8 = rand::thread_rng().gen_range(0, 2);
                    E[i].push(keep);
                    E[j][i] = keep;
                }
                continue;
            }

            if i == j { //avoid loops
                E[i].push(0);
                continue;
            }

            else{
                let keep:u8 = rand::thread_rng().gen_range(0, 2);
                E[i].push(keep);
                E[j].push(keep);
            }
        }
    }
    let graph:G = G { E: (E), N: (N), P: (P) };
    check = bfs(graph.clone());
    if check {
        return graph;
    }
    }
    return graph;
}


// Lattice functions //


//finds the downwards neighbours of a vertex
fn downset (graph:G, v:usize) -> Vec<usize>{
    let count:usize = graph.N as usize;
    let mut res:Vec<usize> = vec![v];
    if v == 0{
        return vec![0];
    }
    for i in 0..count{
        if (graph.E[v][i] == 1) & (graph.P[v] < graph.P[i]){
            res.push(i);
        }
    }
    return res;
}

//finds the join of two vertices in the lattice
pub fn join (graph:G, v:usize, u:usize) -> bool{
    //initialise the down set of v and u
    let mut down_v:Vec<usize> = vec![v];
    let mut down_u:Vec<usize> = vec![u];
    //keeping variables
    let mut down_u_keep:Vec<usize> = vec![];
    let mut down_v_keep:Vec<usize> = vec![];
    // initialise the join set and the cointer for the while loop
    let mut join:Vec<usize> = vec![];
    let mut count:u8;

    let mut stop_u:usize = 0;
    let mut stop_v:usize = 0;
    //initialise a starting position
    if graph.P[v] >= graph.P[u]{
        count = graph.P[v];
    }
    else {
        count = graph.P[u]
    }
    while count > 0{
        // find downset of down_u
        for i in stop_u..down_u.len(){
            down_u_keep = downset(graph.clone(),u);
            for j in 0..down_u_keep.len(){
                down_u.push(down_u_keep[j]);
            }
        }
        stop_u = down_u.len()-1;
        //find downset of down_v
        for i in stop_v..down_v.len(){
            down_v_keep = downset(graph.clone(),v);
            for j in 0..down_v_keep.len(){
                down_v.push(down_v_keep[j]);
            }
        }
        //anoying condition
        stop_v = down_v.len()-1;
        if count == 0{
            break;
        }
        count = count - 1;
    }
    //finds the join set
    for i in 0..down_v.len(){
        if down_u.contains(&down_v[i]){
            join.push(down_v[i]);
        }
    }
    //checks the join condition
    if join.len() > 1{
        println!("false");
        return false
    }

    else {
        println!("true");
        return true;
    }
}