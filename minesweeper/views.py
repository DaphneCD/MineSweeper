from pyramid.view import (
    view_config,
    view_defaults
    )
from services import Game_Service

@view_defaults(renderer='templates/board.pt')
class GameViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {'title_name': 'Welcome to MineSweeper',
                'row_num':'','col_num':'','message':''}

    @view_config(route_name='create_game')#, renderer='json')
    def create_game(self):
        request = self.request
        row_num=int(request.params['row_num'])
        col_num=int(request.params['col_num'])   
        game_service=Game_Service(int(row_num),int(col_num))        
        return game_service.generate_map()

    @view_config(route_name='choose_mine', renderer='json')
    def choose_mine(self):
        request = self.request
        print request
        row_num=int(request.params['row_num'])
        col_num=int(request.params['col_num'])   
        row=int(request.params['row'])
        col=int(request.params['col'])
        game_service=Game_Service(row_num,col_num)  
        updates=game_service.choose_mine(row*col_num+col)
        return updates
        
