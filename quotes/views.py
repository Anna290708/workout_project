from datetime import date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Quote, UserQuoteHistory
from .serializers import QuoteSerializer

class DailyQuoteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        today = date.today()

        today_quote = UserQuoteHistory.objects.filter(user=user, last_seen=today).first()
        if today_quote:
            serializer = QuoteSerializer(today_quote.quote)
            return Response(serializer.data)

        used_quotes = UserQuoteHistory.objects.filter(user=user, seen_count__gte=2).values_list('quote_id', flat=True)
        available_quotes = Quote.objects.exclude(id__in=used_quotes)

        if not available_quotes.exists():
            return Response({"detail": "No more new quotes available."}, status=404)

        quote = available_quotes.order_by('?').first()

        history, created = UserQuoteHistory.objects.get_or_create(user=user, quote=quote)
        if not created:
            history.seen_count += 1
        history.last_seen = today
        history.save()

        serializer = QuoteSerializer(quote)
        return Response(serializer.data)
