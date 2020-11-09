#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
""" Test that passing `more_html = True` collects paragraph styles

:author: Shay Hill
:created: 11/5/2020

Paragraphs can end up nested if there are any tables in the document. Docx2python
un-nests these paragraphs.

```
    <open par 1>
        par 1 text
        <open par 2>
            par 2 text
        <close par 2>
        more par 1 text
    <close par 1>
```

gets flattened to

```
'par 1 text`
`par 2 text`
`more par 1 text`
```

In the output, this will look like three paragraphs. To keep things self-contained,
open/close html tags at the beginning and end of each *output* paragraph.
"""

from docx2python.main import docx2python


class TestParsNestedInTables:
    """ Close html and paragraph tags when paragraphs are nested """

    def test_paragraphs_only(self) -> None:
        """Run without issue"""
        pars = docx2python("resources/CRB EHS Manual.docx", html=True)
        # aaa = pars.document[0][0][0][0]
        # bbb = pars.document[0][0][0]
        # ccc = pars.document[0][0]
        # ddd = pars.document[0]
        breakpoint()
        # assert pars.text == (
        #     "\n\nThis is a document for testing docx2python module.\n\n\n\nThis "
        #     "document contains paragraphs.\n\n\n\nThis document does not contain any "
        #     "bulleted lists.\n\n"
        # )


class TestBulletedLists:
    """Replace numbering format with bullet (--) when format cannot be determined"""

    def test_bulleted_lists(self) -> None:
        pars = docx2python("resources/created-in-pages-bulleted-lists.docx")
        assert pars.text == (
            "\n\nThis is a document for testing docx2python module.\n\n\n\n--\tWhy "
            "did the chicken cross the road?\n\n\t--\tJust because\n\n\t--\tDon't "
            "know\n\n\t--\tTo get to the other side\n\n--\tWhat's the meaning of life, "
            "universe and everything?\n\n\t--\t42\n\n\t--\t0\n\n\t--\t-1\n\n"
        )
