#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: v3.11.0.0git-810-g1ecb8565

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import blocks
import numpy
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import math
import threading



class Lab_comu_3_B(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Lab_comu_3_B")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.n = n = 2
        self.B = B = 10

        ##################################################
        # Blocks
        ##################################################

        self._B_range = qtgui.Range(1, 20, 1, 10, 200)
        self._B_win = qtgui.RangeWidget(self._B_range, self.set_B, "# muestras por simbolo", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._B_win)
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0.set_block_alias("blocks_uchar_to_float_0")
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, B)
        self.blocks_repeat_0.set_block_alias("blocks_repeat_0")
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff((1/math.pow(2,n)))
        self.blocks_multiply_const_vxx_0.set_block_alias("blocks_mu")
        self.blocks_add_const_vxx_0 = blocks.add_const_ff((-(math.pow(2,n)-1)/2))
        self.blocks_add_const_vxx_0.set_block_alias("blocks_add_const_vxx_0")
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, int(math.pow(2,n)), 1000))), False)
        self.analog_random_source_x_0.set_block_alias("analog_random_source_x_0")


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_repeat_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Lab_comu_3_B")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n
        self.blocks_add_const_vxx_0.set_k((-(math.pow(2,self.n)-1)/2))
        self.blocks_multiply_const_vxx_0.set_k((1/math.pow(2,self.n)))

    def get_B(self):
        return self.B

    def set_B(self, B):
        self.B = B
        self.blocks_repeat_0.set_interpolation(self.B)




def main(top_block_cls=Lab_comu_3_B, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
