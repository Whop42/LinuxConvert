from LinuxConvert.software import Software

def test_software_info(Software s):
    assert s.name
    assert s.status == True or s.status = False

if __name__ == "__main__":
    unittest.main()