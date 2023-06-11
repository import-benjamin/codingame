use std::io;
use std::cmp::PartialEq;
use std::fmt::{Display, Formatter, Result};

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}

#[derive(PartialEq, Debug)]
struct Node {
    pub x: i32,
    pub y: i32,
}

const EMPTY_NODE: Node = Node {x: -1, y: -1};

impl Display for Node {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        write!(f, "{} {}", self.x, self.y)
    }
}

fn read_input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim_matches('\n').to_string()
}

fn parse_line(y: i32, line: String) -> Vec<Node> {
    eprintln!("parsing line {}: {}", y, line);
    line.chars()
        .enumerate()
        .map(|(i, c)| match c {
            '0' => Node { x: i as i32, y: y},
            _ => EMPTY_NODE
        })
        .collect()
}

fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let width = parse_input!(input_line, i32);
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let height = parse_input!(input_line, i32);
    eprintln!("dimensions: w{width} h{height}");

    let rendered_line = ".".repeat(width as usize);
    let mut curr: Vec<Node> = parse_line(0, read_input());

    let remove_empty_nodes = move |&(_, v): &(_, &Node)| -> bool {
        match *v {
            Node {x, y} if (x == -1) && (y == -1) => false,
            _ => true}
    };

    for i in 1..(height+1) {
        let content: String = if i == height { rendered_line.to_string() } else { read_input() };
        
        let next = parse_line(i as i32, content);

        let curr_nodes = curr.iter()
            .enumerate()
            .filter(remove_empty_nodes);

        curr_nodes
            .for_each(
                |(i,v)| println!(
                    "{} {} {}",
                    v,
                    curr.iter()
                        .enumerate()
                        .filter(remove_empty_nodes)
                        .find(|&(li, _)| li > i)
                        .unwrap_or_else(|| (0, &EMPTY_NODE)).1,
                    next.get(i).unwrap_or_else(|| &EMPTY_NODE)
                )
            );

        curr = next;
    };

}
