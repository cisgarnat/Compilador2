ANTLR_JAR=lib/antlr-4.13.2-complete.jar
GRAMMAR=src/ConsultaSQL.g4
OUT=src/

antlr:
	java -jar $(ANTLR_JAR) -Dlanguage=Python3 $(GRAMMAR) -visitor -o $(OUT)

run:
	python3 src/main.py

test:
	pytest tests/

clean:
	rm -f src/*.interp src/*.tokens
