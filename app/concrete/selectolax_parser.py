from app.interfaces.parser import Parser


class SelectolaxParser(Parser):
    def __init__(self, html_parser, currency_to_float_func, average_price_func):
        self.html_parser = html_parser
        self.currency_to_float_func = currency_to_float_func
        self.average_price_func = average_price_func

    def compras_paraguai_item_average_price(self, content: str | bytes) -> float:
        try:
            html_content = self.html_parser(content)
            container = html_content.css_first("#compare")
            elements = container.css(".promocao-item-preco-text")
            if len(elements) == 0:
                raise Exception("The elements with selector '.promocao-item-preco-text' does not exist.")
            price_list = [self.currency_to_float_func(e.text()) for e in elements]
            average_price = self.average_price_func(price_list)
            return average_price
        except Exception:
            # TODO: Log the exception
            return 0.0

    def compras_paraguai_item_main_url(self, content: bytes) -> str | None:
        parsed = self.html_parser(content)
        first_child = parsed.css_first('.row.resultados-busca > :first-child')
        if first_child is not None:
            return first_child.css_first('a').attributes['href']
        return None