use osu_syncflow::file::read_osu_file;

#[test]
fn test_read_osu_file_success() {
    let content = read_osu_file("assets/reanimate/reanimate.osu").expect("Failed to read file.");
    assert!(content.contains("[HitObjects]"));
}

#[test]
fn test_read_osu_file_not_found() {

}

