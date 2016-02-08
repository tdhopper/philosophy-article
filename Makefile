
dependencies:
	STATIC_DEPS=true pip install -Ur requirements.txt -t .

prepare: dependencies
	rm -f lambda_bundle.zip
	zip -r lambda_bundle *
	make clean

clean:
	git clean -fd