all:
	rm -rf bin/
	mkdir bin
	chmod +x parser_test.py
	chmod +x parser4.py
	cp parser_test.py bin/parser
	cp lexer.py bin/lexer.py
	cp ptg.cpp bin/ptg.cpp
	cp dtg.cpp bin/dtg.cpp
	cp dotgen.sh bin/dotgen.sh
	cp parser4.py bin/parser4
	cp Symbol_Table.py bin/Symbol_Table.py
	cp ST2.py bin/ST2.py
	cp ThreeAddrCode.py bin/ThreeAddrCode.py

clean:
	rm -rf bin/
	rm output.txt output1.txt a.out parser.out parselog.txt parsetab.py parsetree.ps parse_tree.dot
