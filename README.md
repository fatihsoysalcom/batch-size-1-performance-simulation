# Batch Size 1 Performance Simulation

This example simulates the performance difference when generating multiple items one by one (batch size 1) versus processing them in a single batch. It highlights how fixed overheads per inference call can significantly slow down operations when not amortized across a larger batch, a common issue in image generation models.

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [Neden Görüntü Üretme Modelleriniz Batch Size 1'de Yavaş? Gerçek Çözümler Nelerdir?](https://fatihsoysal.com/blog/neden-goruntu-uretme-modelleriniz-batch-size-1de-yavas-gercek-cozumler-nelerdir/).

## License

MIT — see [LICENSE](LICENSE).
