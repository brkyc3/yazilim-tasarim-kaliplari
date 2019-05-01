def _find_similars(image, count):
    similar_ids = []
    return similar_ids


def _connect_db():
    return None


class SimilarImages:

    def __init__(self, image, count=10):
        self._image_ids = _find_similars(image, count)
        self._db_connection = _connect_db()

    def _get_image(self, image_id):
        return self._db_connection.query_image(image_id)

    def __iter__(self):
        self._cur_item = 0
        return self

    def __next__(self):
        if self._cur_item is len(self._image_ids):
            raise StopIteration()
        image = self._get_image(self._image_ids[self._cur_item])
        self._cur_item += 1

        return image


