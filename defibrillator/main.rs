use std::io;

macro_rules! parse_input {
    ($x:expr, $t:ident) => ($x.trim().parse::<$t>().unwrap())
}


fn as_float(s: &str) -> f64 {
    return s.replace(',', ".").parse::<f64>().expect("Can't parse value {s}.");
}

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
fn main() {
    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();

    let lon = as_float(input_line.trim());


    eprintln!("lon: {lon}");


    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let lat = as_float(input_line.trim());

    let mut input_line = String::new();
    io::stdin().read_line(&mut input_line).unwrap();
    let n = parse_input!(input_line, i32);

    let mut close_defibrilator = std::f64::MAX;
    let mut close_defibrilator_name: String = String::from("NONE");

    eprintln!("close_defibrilator: {close_defibrilator}");

    for i in 0..n as usize {
        let mut input_line = String::new();
        io::stdin().read_line(&mut input_line).unwrap();
        let defib = input_line.trim_matches('\n').to_string();
        let s_defib = defib.split(';').collect::<Vec<&str>>();
        let lo = as_float(s_defib.get(4).expect("Can't read value lo.").to_owned());
        let la = as_float(s_defib.get(5).expect("Can't read value lo.").to_owned());

        eprintln!("line: {defib}\nlo: {lo}\nla: {la}");

        let x = (lo - lon) * ((lat + la)/2.0).cos();
        let y = (la - lat);
        
        let d  = (x*x + y*y).sqrt() * 6371.0;

        if (close_defibrilator > d) {
            let name = s_defib.get(1).expect("Can't get defibrilator name.").to_owned().to_string();
            close_defibrilator_name = String::from(name);
            close_defibrilator = d;
        }
        
    }

    // Write an answer using println!("message...");
    // To debug: eprintln!("Debug message...");

    println!("{close_defibrilator_name}");
}
