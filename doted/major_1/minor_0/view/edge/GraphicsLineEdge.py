# -*- coding: utf-8 -*-

# Copyright (c) 2016 Victor Nea, Morvan Lassauzay, Matthieu Dien, Marwan Ghanem
# This file is part of dotEd.
#
# dotEd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dotEd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dotEd.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.Qt import QPainterPath, QPainterPathStroker
from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsItem

from doted.major_1.minor_0.utils.EdgeUtils import EdgeUtils
from doted.major_1.minor_0.view.edge.GraphicsEdge import GraphicsEdge


class GraphicsLineEdge(GraphicsEdge, QGraphicsLineItem):
    '''The GraphicsLineEdge defines a graphics edge as a simple line.


    Argument(s):
    source (GraphicsNode): Node view
    dest (GraphicsNode): Node view
    id (int): ID
    graphicsGraphView (GraphicsGraphView): View
    '''

    def __init__(self, source, dest, id, graphicsGraphView):
        # Parent constructor(s)
        GraphicsEdge.__init__(self, source, dest, id, graphicsGraphView)
        QGraphicsLineItem.__init__(self)

        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.update()

    def update(self):
        '''Update the coordinates of the line.'''
        # Get the two shapes of each node
        sourceShape = self.source.mapToScene(self.source.shape())
        destShape = self.dest.mapToScene(self.dest.shape())

        # Compute the closest points between the two shapes
        pSource = EdgeUtils.closestPointTo(destShape.boundingRect().center(),
                                           sourceShape)
        pDest = EdgeUtils.closestPointTo(sourceShape.boundingRect().center(),
                                         destShape)

        # Draw a line between source and dest
        self.setLine(pSource.x(), pSource.y(), pDest.x(), pDest.y())

    def shape(self):
        '''Defines the selection shape of the item.'''
        stroker = QPainterPathStroker()

        # Tolerance on click to update if needed
        stroker.setWidth(12)

        path = QPainterPath()
        path.moveTo(self.line().p1())
        path.lineTo(self.line().p2())

        return stroker.createStroke(path)
