from ucimlrepo import fetch_ucirepo
import pandas as pd

class IrisDataAnalyzer:
    def __init__(self):
        self.iris = None
        self.X = None  # Features
        self.y = None  # Targets

    def load_data(self):
        self.iris = fetch_ucirepo(id=53)
        self.X = self.iris.data.features
        self.y = self.iris.data.targets

    def display_metadata(self):
        print("Dataset Metadata: ")
        print(self.iris.metadata)

    def display_variables(self):
        print("Variable Information:")
        print(self.iris.variables)

    def preview_data(self, n=5):
        print("\nPreview of Features: ")
        print(self.X.head(n))
        print("Preview of Targets: ")
        print(self.y.head(n))

def main():
    analyzer = IrisDataAnalyzer()
    analyzer.load_data()
    analyzer.display_metadata()
    analyzer.display_variables()
    analyzer.preview_data()

if __name__ == "__main__":
    main()
