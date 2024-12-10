use std::collections::HashMap;
use serde::Deserialize;
use serde_json;

use std::fs::{self, File};
use std::io::Write;

#[derive(Debug, Deserialize)]
struct Config {
    format_version: String,
    sections: HashMap<String, HashMap<String, String>>,
}

fn load_template(path: &str) -> Result<Config, Box<dyn std::error::Error>> {
    let file = std::fs::File::open(path)?;
    let config: Config = serde_json::from_reader(file)?;

    Ok(config)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = load_template("../assets/wip_template.json")?;

    let mut file = File::create("../out/test_out.osu")?; 
    writeln!(file, "{}\n", &config.format_version);

    for (section_name, fields) in &config.sections {
        writeln!(file, "[{}]", section_name);

        for (field_name, field_type) in fields {
            writeln!(file, "{}: {}", field_name, field_type);
        }

        writeln!(file, "\n");
    }  

    Ok(())
}
