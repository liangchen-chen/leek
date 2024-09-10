#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 22:40
# @Author  : shenglin.li
# @File    : strategy_chan_test.py
# @Software: PyCharm
import decimal
import unittest

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go

from leek.common import EventBus
from leek.runner.view import ViewWorkflow
from leek.strategy.common import PositionDirectionManager
from leek.strategy.common.strategy_common import PositionRateManager
from leek.strategy.common.strategy_filter import JustFinishKData, DynamicRiskControl
from leek.strategy.strategy_chan import ChanStrategy
from leek.strategy.strategy_rsi import RSIStrategy
from leek.strategy.strategy_td import TDStrategy
from leek.trade.trade import PositionSide


class TestChan(unittest.TestCase):
    def test_handle(self):
        self.strategy = ChanStrategy()

        self.bus = EventBus()
        # workflow = ViewWorkflow(self.strategy, "5m", "2024-06-28", "2024-07-01", "AEVO-USDT-SWAP")
        # workflow = ViewWorkflow(self.strategy, "5m", "2024-07-14", "2024-07-25", "ULTI-USDT-SWAP")
        workflow = ViewWorkflow(self.strategy, "5m", "2024-07-18 23:10", "2024-07-21 20:00", "ULTI-USDT-SWAP")
        # workflow = ViewWorkflow(self.strategy, "5m", "2024-07-17 08:20", "2024-07-19 20:30", "ULTI-USDT-SWAP")

        workflow.start()
        df = pd.DataFrame([x.__json__() for x in workflow.kline_data_g])
        # df.to_csv("data.csv")
        df['Datetime'] = pd.to_datetime(df['timestamp'] + 8 * 60 * 60 * 1000, unit='ms')
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
        # df["benchmark"] = df["close"] / df.iloc[1]["close"]
        # df["profit"] = df["balance"] / decimal.Decimal("1000")
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['benchmark'], mode='lines', name='benchmark'), row=2, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['chan_point'], mode='lines', line=dict(color='black', width=1), name='chan b', connectgaps=True), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Datetime'], y=df['segment'], mode='lines', line=dict(color='blue', width=2), name='segment', connectgaps=True), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['high'], mode='lines', line=dict(color='green', width=1), name='chan h', connectgaps=True), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['low'], mode='lines', line=dict(color='red', width=1), name='chan l', connectgaps=True), row=1, col=1)
        # fig.add_trace(go.Scatter(
        #     x=df['Datetime'],
        #     y=df['bottom'] * decimal.Decimal("0.98"),
        #     mode='markers+text',
        #     text="底分",
        #     marker=dict(color='green', size=4)
        # ), row=1, col=1)
        #
        # fig.add_trace(go.Scatter(
        #     x=df['Datetime'],
        #     y=df['top'] * decimal.Decimal("1.02"),
        #     mode='markers+text',
        #     text="顶分",
        #     marker=dict(color='red', size=4)
        # ), row=1, col=1)
        # fig.add_trace(go.Scatter(x=df['Datetime'], y=df['profit'], mode='lines', name='profit'), row=2, col=1)
        # fig.add_trace(go.Candlestick(x=df['Datetime'],
        #                              open=df['chan_low'],
        #                              high=df['chan_high'],
        #                              low=df['chan_low'],
        #                              close=df['chan_high'], name=df.iloc[0]["symbol"]), row=2, col=1)
        # fig.update_xaxes(rangeslider_visible=False, row=1, col=1)
        # fig.update_xaxes(rangeslider_visible=False, row=2, col=1)
        workflow.draw(fig=fig, df=df)
        fig.show()


if __name__ == '__main__':
    unittest.main()