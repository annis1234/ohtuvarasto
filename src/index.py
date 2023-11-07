from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("\nOlutvarasto:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print("\nMehuvarasto:")
    print(f"saldo = {mehua.saldo}")
    print(f"tilavuus = {mehua.tilavuus}")
    print(f"paljonko_mahtuu = {mehua.paljonko_mahtuu()}")

if __name__ == "__main__":
    main()
