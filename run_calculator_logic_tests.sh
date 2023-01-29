echo "Running tests for the Calculator"
echo ""
python3 -m coverage run -m unittest src/tests/calculator/TestFakeParser.py src/tests/calculator/TestFakeScanner.py src/tests/calculator/TestScannerInternalMethods.py src/tests/calculator/TestUtilities.py

# echo ""
# echo "Running tests for the Fake Scanner"
# echo ""
# python3 -m coverage run -m unittest src/tests/calculator/TestFakeScanner.py
# python3 -m coverage run -m unittest src/tests/calculator/TestScannerInternalMethods.py

# echo ""
# echo "Running tests for the Utilities"
# echo ""
# python3 -m coverage run -m unittest src/tests/calculator/TestUtilities.py

echo ""
echo "Test Coverage"
echo ""
python3 -m coverage report