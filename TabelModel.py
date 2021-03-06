from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Model(QAbstractTableModel):
    def __init__(self, parent=None, matrix=[[0], [0]], *args):
        QAbstractTableModel.__init__(self, parent, *args)
        print(*args)
        self.added = 0
        self.matrix = matrix

    def rowCount(self, parent=QModelIndex()):
        return len(self.matrix)

    def columnCount(self, parent=QModelIndex()):
        return len(self.matrix[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()

        row = index.row()
        column = index.column()
        if row < len(self.matrix) and column < len(self.matrix[0]):
            return QVariant(self.matrix[row][column])
        else:
            return QVariant()

    def removeRows(self, position, rows=1, index=QModelIndex()):
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)
        self.items = self.items[:position] + self.items[position + rows:]
        self.endRemoveRows()

        return True

    def insertRows(self, position, rows=1, index=QModelIndex()):
        indexSelected = self.index(position, 0)
        itemSelected = indexSelected.data().toPyObject()

        self.beginInsertRows(QModelIndex(), position, position + rows - 1)
        for row in range(rows):
            self.items.insert(position + row, "%s_%s" % (itemSelected, self.added))
            self.added += 1
        self.endInsertRows()
        return True
