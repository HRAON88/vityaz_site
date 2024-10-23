document.addEventListener('DOMContentLoaded', function() {
    const scheduleButton = document.getElementById('getSchedule');
    if (scheduleButton) {
        scheduleButton.addEventListener('click', function() {
            const kind_of_sport = document.getElementById('kind_of_sport').value;
            const age = document.getElementById('age').value;

            const daysOfWeek = {
                0: 'Понедельник',
                1: 'Вторник',
                2: 'Среда',
                3: 'Четверг',
                4: 'Пятница',
                5: 'Суббота',
                6: 'Воскресенье'
            };

            fetch(`/api/schedule/${age}/${kind_of_sport}/`)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById('scheduleTable').innerHTML = `<p>${data.error}</p>`;
                    } else {
                        let tableHTML = `<table><tr><th>Группа</th><th>День недели</th><th>Начало</th><th>Конец</th><th>Тренер</th></tr>`;
                        data.forEach(schedule => {
                            const dayName = daysOfWeek[schedule.day_of_week] || 'Неизвестный день';
                            tableHTML += `<tr>
                                <td>${schedule.group.name}</td>
                                <td>${dayName}</td>
                                <td>${schedule.start_time}</td>
                                <td>${schedule.end_time}</td>
                                <td>${schedule.group.trainer}</td>
                              </tr>`;
                        });
                        tableHTML += '</table>';
                        document.getElementById('scheduleTable').innerHTML = tableHTML;
                    }
                })
                .catch(error => console.error('Error fetching schedule:', error));
        });
    } else {
        console.error('Button with ID "getSchedule" not found.');
    }
});
