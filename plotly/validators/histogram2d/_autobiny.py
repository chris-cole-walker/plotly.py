import _plotly_utils.basevalidators


class AutobinyValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='autobiny', parent_name='histogram2d', **kwargs
    ):
        super(AutobinyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            implied_edits={},
            role='style',
            **kwargs
        )